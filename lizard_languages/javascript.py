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
                   r"|(?:\<\w+\>)" + \
                   r"|(?:\<\/\w+\>)" + \
                   r"|`.*?`" + \
                   r"|/>" + \
                   r"|(?:\w+\?)"
        return CodeReader.generate_tokens(source_code, addition, token_class)

    def __init__(self, context):
        super(JavaScriptReader, self).__init__(context)
        self.parallel_states = [JavaScriptStyleLanguageStates(context)]
