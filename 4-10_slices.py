# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that prints three slices of the list.

numbers = []

for number in range(1, 11):
    numbers.append(number**3)

print(numbers[:3])
print(numbers[4:7])
print(numbers[7:])