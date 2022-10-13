print(type("hello world"))

'''
class str
fundamental data type
sequence data type - each character has a index!
can use '' or ""
' "" '
" '' "
''' '''
""" """
Can contain any Unicode character - contains Emoji
'''
string = "He said \"What time is it \""

len(string) # including spaces

'''
PEP8 - style guide

break line in strings using 
 - backslash
 - ''' '''
 - """ """ 
'''


"""
Concatenation: string1 + string2
Indexing: my_string[3], index -1 is the last element
Slice: creating substring - dessert = "apple pie" => dessert[0:5] => "apple"
"""

dessert = 'apple pie'
print(dessert[:5]) # apple
print(dessert[6:]) # pie
print(dessert[:]) # apple pie

"""
String are immutable! - returns a TypeError!
"""
word = 'programming'
word[0] = 'a'






