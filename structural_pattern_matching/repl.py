import ast
import sys
import traceback

PROMPT = "\N{snake} "

COMMANDS = ('help', 'exit', 'quit')


def main():
    while True:
        try:
            match input(PROMPT):
                case command if command.lower() in COMMANDS:  # optional guard clause
                    match command.lower():
                        case 'help':
                            print('Display help')
                        case 'exit' | 'quit':
                            print('Exiting...')
                            break
                case expression if valid(expression, "eval"):
                    """Store last variable by _"""
                    _ = eval(expression)
                    if _ is not None:
                        print(_)
                case statement if valid(statement, "exec"):
                    exec(statement)
                case _:
                    """Needs to go as a last statement"""
                    print("Type a valid Python command")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
        except EOFError:
            print()
            exit()
        except Exception:
            traceback.print_exc(file=sys.stdout)


def valid(code, mode):
    """
        Using built in Abstract Syntax Tree parser.

        passing 2+2 as expression is not executed with visible (returned) result by exec() function
    """
    try:
        ast.parse(code, mode)
        return True
    except SyntaxError:
        return False



if __name__ == '__main__':
    main()
