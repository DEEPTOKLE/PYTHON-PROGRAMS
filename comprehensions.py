numbers = [1, 2, 3, 4, 5]

list_comprehension = [n * n for n in numbers]
print("List Comprehension:", list_comprehension)

dictionary_comprehension = {n: n * n for n in numbers}
print("Dictionary Comprehension:", dictionary_comprehension)

set_comprehension = {n * n for n in numbers}
print("Set Comprehension:", set_comprehension)