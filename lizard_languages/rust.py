'''
Language parser for Go lang
'''

from .clike import CCppCommentsMixin
from .code_reader import CodeReader
from .golike import GoLikeStates


class RustReader(CodeReader, CCppCommentsMixin):
    # pylint: disable=R0903

    ext = ['rs']
    language_names = ['rust']
    _conditions = {
        'if', 'for', 'while', '&&', '||', '?', 'catch',
        'case', 'match', 'where'
    }

    def __init__(self, context):
        super(RustReader, self).__init__(context)
        self.parallel_states = [RustStates(context)]


class RustStates(GoLikeStates):  # pylint: disable=R0903
    FUNC_KEYWORD = 'fn'
