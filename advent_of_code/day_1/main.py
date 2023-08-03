elements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

with open('input.txt') as f:
    data = f.read().split('\n')
    print(data)


def count_larger(numbers):
    counter = 0
    for i, elem in enumerate(numbers):
        if elem > numbers[i - 1]:
            counter += 1

    return counter


def shorter_large_counter(numbers):
    return len([elem for index, elem in enumerate(numbers) if int(elem) > int(numbers[index-1])])


assert 7 == count_larger(elements)
assert 7 == shorter_large_counter(elements)


with open('input.txt') as f:
    data = f.read().split('\n')
    print(shorter_large_counter(data))