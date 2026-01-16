import random

x = random.randrange(1, 10)
y = random.randrange(1, 10)

answer = int(input(f"What's {x} multiplied by {y}? "))
expected = x * y

print("answer:", answer)
print("expected:", expected)

# self documenting expressions
print(f"{answer = }")
print(f"{expected = }")

if answer == expected:
    print("Correct!")
else:
    print("That's incorrect")