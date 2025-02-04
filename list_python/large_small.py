def find_largest_smallest(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    return largest, smallest
num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
largest, smallest = find_largest_smallest(num_list)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")