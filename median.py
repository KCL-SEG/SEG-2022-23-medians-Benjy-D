"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
numbers.sort()
if len(numbers) % 2 == 0:
    midpoint = int(len(numbers) / 2)
    middle = (numbers[midpoint-1] + numbers[midpoint]) / 2
else:
    middle = numbers[len(numbers) // 2]

print(numbers)
print(middle)
