''' programming languages of lizard '''

from .clike import CLikeReader
from .csharp import CSharpReader
from .fortran import FortranReader
from .gdscript import GDScriptReader
from .go import GoReader
from .java import JavaReader
from .javascript import JavaScriptReader
from .kotlin import KotlinReader
from .lua import LuaReader
from .objc import ObjCReader
from .php import PHPReader
from .python import PythonReader
from .ruby import RubyReader
from .rust import RustReader
from .scala import ScalaReader
from .swift import SwiftReader
from .ttcn import TTCNReader


def languages():
    return [
        CLikeReader,
        JavaReader,
        CSharpReader,
        JavaScriptReader,
        PythonReader,
        ObjCReader,
        TTCNReader,
        RubyReader,
        PHPReader,
        SwiftReader,
        ScalaReader,
        GDScriptReader,
        GoReader,
        LuaReader,
        RustReader,
        FortranReader,
        KotlinReader
    ]


def get_reader_for(filename):
    for lan in languages():
        if lan.match_filename(filename):
            return lan
