"""
Assuming that we have some email addresses in the "username@companyname.com" format,
\please write program to print the company name of a given email address.
Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.
"""
import re


def email_company_name(email_address: str):
    pattern = "(\w+)@((\w+))"
    matched = re.match(pattern, email_address)

    return matched.group(2)


print(email_company_name("john@google.com"))
