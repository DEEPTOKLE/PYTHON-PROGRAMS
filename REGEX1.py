import re

prog = re.compile(r'm\w\w')

str = 'cat mat rat bat'
result = prog.search(str)
print(result.group())

str1 = 'Operating System format'
result = prog.search(str1)
print(result.group())