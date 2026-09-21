import re

prog = re.compile(r'm\w\w')

str = input('Enter string')
result = prog.search(str)

if result:
    print(result.group())
else:
    print('Match not found')