# TODO: Complete the get_ruler function
def get_ruler(kingdom):
    # TODO: Add logic to determine the ruler of the kingdom
    # It should be either 'Alice', 'Bob' or 'nobody'.
    ruler = ('Alice', 'Bob', 'nobody')
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    last_kingdom_letter = kingdom[-1]

    if last_kingdom_letter in vowels:
        return ruler[0]

    if last_kingdom_letter == 'y':
        return ruler[2]

    return ruler[1]


def main():
    # Get the number of test cases
    T = 3

    kingdoms = [
        'Mollaristan',
        'Auritania',
        'Zizily'
    ]

    for t in range(T):
        # Get the kingdom
        kingdom = kingdoms[t]

        print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))


if __name__ == '__main__':
    main()

"""
Case #1: Mollaristan is ruled by Bob.
Case #2: Auritania is ruled by Alice.
Case #3: Zizily is ruled by nobody.
"""
