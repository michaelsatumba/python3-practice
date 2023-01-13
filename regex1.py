import re

phoneNumRgx = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d)')
mo = phoneNumRgx.search('hello (012) 345-6789')
print(mo.group())
first = mo.group(1)
second = mo.group(2)
# allOfGroup = mo.group(0) # same as mo.group()

print('first ' + first)
print('second ' + second)

batRegex = re.compile(r'Bat(man|mobile|copter)')
batMo = batRegex.search('Batman and Batmobile')
print(batMo.group(1))



