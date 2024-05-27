
num1 = 2
num2 = 3
lcm = 0

maximum = max(num1, num2)

count = maximum


if maximum % num2 == 0 and maximum % num1 == 0:
    lcm = maximum
    maximum = maximum + 1

else:
    lcm = 999


print(lcm)
