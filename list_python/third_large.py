num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
num_list.sort(reverse=True)
if len(num_list) < 3:
    print("List must contain at least three numbers.")
else:
    print("Third largest number:", num_list[2])