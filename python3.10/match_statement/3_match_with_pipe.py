# Usage of match pattern with pipe (|) statement.
# OrPattern

# PEP 634, PEP 635, PEP 636

lang_prefix = 'PY'

class LangPrefix:
    PYTHON_PREFIX = 'P'
    PYTHON_PREFIX_V2 = 'PY'
    RUST_PREFIX = 'R'
    JAVA_PREFIX = 'J'


match lang_prefix:
    case LangPrefix.PYTHON_PREFIX | LangPrefix.PYTHON_PREFIX_V2:
        print('PYTHON')
    case LangPrefix.RUST_PREFIX:
        print('RUST')
    case LangPrefix.JAVA_PREFIX:
        print('JAVA')


