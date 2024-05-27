nums = input("Enter the integers separated by spaces: ")

my_list = [int(i) for i in nums.split()]

total = sum(my_list)

print(f'The su of the integers is :{total}')