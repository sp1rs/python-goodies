# Basic usage of switch. Matching against literal constant.

lang_prefix = 'P'

match lang_prefix:
    case 'P':
        print('PYTHON')
    case 'R':
        print('RUST')
    case 'J':
        print('JAVA')


