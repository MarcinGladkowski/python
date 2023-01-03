import re

text = 'There are some things in 1962'

print(re.findall('[\d]', text))

'''

* Qualifiers

\w -> any word character (also unicode)
\W -> opposite to any word character
\d -> digit
\D -> not digit
\s -> whitespace (space, tab, p, nbsp - non break whitespace)
\S -> not whitespace
\b -> boundary
\B -> not boundary
'''

'''
* Identifiers
'a|b|c' -> or
'''

'''
*Quantifiers
{5} -> five lements

* Greedy - chciwy

re.findall('[a-z]{2, 4}', text) # get longest if exists

* Lazy - leniwe

re.findall('[a-z]{2,}', text)
 
re.findall('[a-z]{2,4}?', text) # prefer shortest!

re.findall('\d+', text)  -> min 1 digit

+ -> min 1
* -> min zero {0,}
? -> zero or one {0,1}

'''

re.findall('[a-z]{4}', text) # all four characters words

re.findall(r'\b[a-z]{4}\b', text) # boundary example

'''
. -> any character
.* -> any character of any count
'''


'''
* Grouping
By using ()
'''
re.search(r'(?P<rok>\d{4})', text).groupdict() # {rok: 1926}

'''
* keyword groups
* non matching groups (?:....) -> to ignore them
'''
