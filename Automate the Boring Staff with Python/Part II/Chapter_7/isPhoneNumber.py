import re


phoneMumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office. another 415-555-1000'

mo = phoneMumRegex.search(message)
print(f"Phone number found: {mo.group()}")