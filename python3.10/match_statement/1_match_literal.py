# Basic usage of Match statement. 
# Literal Pattern

# PEP 634, PEP 635, PEP 636

lang_prefix = 'P'

match lang_prefix:
    case 'P':
        print('PYTHON')
    case 'R':
        print('RUST')
    case 'J':
        print('JAVA')
