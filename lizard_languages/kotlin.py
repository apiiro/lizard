'''
Language parser for Apple Swift
'''

from .clike import CCppCommentsMixin
from .code_reader import CodeReader
from .golike import GoLikeStates


class KotlinReader(CodeReader, CCppCommentsMixin):
    # pylint: disable=R0903

    ext = ['kt', 'kts']
    language_names = ['kotlin']
    _conditions = {
        'if', 'for', 'while', 'when', '->', 'catch', '&&', '||', '?:'
    }

    def __init__(self, context):
        super(KotlinReader, self).__init__(context)
        self.parallel_states = [KotlinStates(context)]

    @staticmethod
    def generate_tokens(source_code, addition='', token_class=None):
        return CodeReader.generate_tokens(
            source_code,
            r"|`\w+`" +
            r"|\w+\?" +
            r"|\w+\!!" +
            r"|\?\?" +
            addition
        )

    def preprocess(self, tokens):
        return list(t for t in tokens if not t.isspace() or t == '\n')


class KotlinStates(GoLikeStates):  # pylint: disable=R0903

    FUNC_KEYWORD = 'fun'

    def _state_global(self, token):
        if token in {'->'}:
            self.context.push_new_function('')
            self.next(self._function_name, token)
        elif token in ('get', 'set'):
            self.context.push_new_function(token)
            self._state = self._expect_function_impl
        elif token in ('val', 'var', ','):
            self._state = self._expect_declaration_name
        else:
            super(KotlinStates, self)._state_global(token)

    def _expect_declaration_name(self, token):
        self._state = self._state_global
