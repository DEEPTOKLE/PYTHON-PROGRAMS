import re

prog = re.compile(r'k\w\w')

str = input('Enter string: ')

result = re.findall(r'm\w\w', str)

if result:
    print(result)
else:
    print('Match not found')