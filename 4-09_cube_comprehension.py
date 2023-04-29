# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

numbers = []

for number in range(1, 11):
    numbers.append(number**3)

print(numbers)