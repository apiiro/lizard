'''
Language parser for JavaScript
'''

from .clike import CCppCommentsMixin
from .code_reader import CodeReader
from .js_style_language_states import JavaScriptStyleLanguageStates
from .js_style_regex_expression import js_style_regex_expression


class JavaScriptReader(CodeReader, CCppCommentsMixin):
    # pylint: disable=R0903

    ext = ['js', 'jsx', 'ts', 'tsx']
    language_names = ['javascript', 'js', 'typescript', 'ts']

    _conditions = {
        'if', 'elseif', 'for', 'while', '&&', '||', '?',
        'catch', 'case'
    }

    @staticmethod
    @js_style_regex_expression
    def generate_tokens(source_code, addition='', token_class=None):
        addition = addition + \
                   r"|(?:\$\w+)" + \
                   r"|(?:\<\/\w+\>)" + \
                   r"|`.*?`" + \
                   r"|(?:\w+\?)"
        js_tokenizer = JSTokenizer()
        for token in CodeReader.generate_tokens(
                source_code, addition, token_class):
            for tok in js_tokenizer(token):
                yield tok

    def __init__(self, context):
        super(JavaScriptReader, self).__init__(context)
        self.parallel_states = [JavaScriptStyleLanguageStates(context)]


class Tokenizer(object):
    def __init__(self):
        self.sub_tokenizer = None
        self._ended = False

    def __call__(self, token):
        if self.sub_tokenizer:
            for tok in self.sub_tokenizer(token):
                yield tok
            if self.sub_tokenizer._ended:
                self.sub_tokenizer = None
            return
        for tok in self.process_token(token):
            yield tok

    def stop(self):
        self._ended = True

    def process_token(self, token):
        pass


class JSTokenizer(Tokenizer):
    def __init__(self):
        super(JSTokenizer, self).__init__()
        self.depth = 1

    def process_token(self, token):
        if token == "{":
            self.depth += 1
        elif token == "}":
            self.depth -= 1
            if self.depth == 0:
                self.stop()
                # {} in JSX is not listed as token
                # otherwise it will be regarded
                # as JS object
                return
        yield token
