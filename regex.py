import re

message = 'Call me at 123-456-789d'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# print(phoneNumRegex)

mo = phoneNumRegex.search(message)
# print(mo)


if mo == 'None':
    result = mo.group()
    print(result)
else:
    print('no number found')


