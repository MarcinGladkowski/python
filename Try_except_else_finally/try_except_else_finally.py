'''
Else statement allows to show clear what happen after successful
executing try block. Optimize try block
'''


import json


UNDEFINED = object()



def divide_json(path):
    '''
        Possible errors are described in comments
    '''
    print('* Open file')
    handle = open(path, 'r+') # OSError
    try:
        print('* Read data')
        data = handle.read() # UnicodeDecodeError
        print('* Load data JSON')
        op = json.loads(data) # ValueError
        print('* Processing data')
        value = (
            op['numerator'] / op['denominator']
        ) # ZeroDivisionError
    except ZeroDivisionError as e:
        print('* Catch ZeroDivisionError')
        return UNDEFINED
    else:
        print('* Saving data')
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)           # OSError
        handle.write(result)     # OSError
        return value
    finally:
        print('* Call close() function')
        handle.close()