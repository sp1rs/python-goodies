# Basic usage of Match statement. 
# Value Pattern

# PEP 634, PEP 635, PEP 636


lang_prefix = 'P'

class LangPrefix:
    PYTHON_PREFIX = 'P'
    RUST_PREFIX = 'R'
    JAVA_PREFIX = 'J'


match lang_prefix:
    case LangPrefix.PYTHON_PREFIX:
        print('PYTHON')
    case LangPrefix.RUST_PREFIX:
        print('RUST')
    case LangPrefix.JAVA_PREFIX:
        print('JAVA')
    case _:
        print('No Matched Found')

