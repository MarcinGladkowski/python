

PROMPT = "\N{snake} "

COMMANDS = ('help', 'exit', 'quit')


def main():
    while True:
        match input(PROMPT):
            case command if command.lower() in COMMANDS: # optional guard clause
                match command.lower():
                    case 'help':
                        print('Display help')
                    case 'exit' | 'quit':
                        print('Exiting...')
                        break

if __name__ == '__main__':
    main()