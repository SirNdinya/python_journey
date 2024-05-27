nums = input("Enter set one integers separated by spaces: ")
nums2 = input("Enter set two integers separated by spaces: ")

set_one = set(nums.split())
set_two = set(nums2.split())
set_three = set_one.intersection(set_two)

print("Common Elements:", set_three)