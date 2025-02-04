numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
even_numbers = sorted([num for num in numbers if num % 2 == 0])
print("Even numbers in ascending order:", even_numbers)