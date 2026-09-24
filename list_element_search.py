numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the number to search: "))

found = False

for index, number in enumerate(numbers):
    if number == target:
        print("Element found at position:", index)
        found = True
        break

if not found:
    print("Element not found.")
