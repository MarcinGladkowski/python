'''
try-except
'''

nums = []

for x in range(5):
    try:
        x = int(input())
    except ValueError as e:
        x = 0
        print(e)
    except Exception as e:
        print(e)
    else:
        print('correct number')
    finally:
        print('number appended')
        nums.append(x)

for x in range(5):
    print(nums[x])
