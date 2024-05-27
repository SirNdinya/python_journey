
my_list = list() # creating an empty list


# list with elements

my_list2 = ['football', 'volleyball', 'handball', 'hockey']

len(my_list2) # returns the length of the list

my_list2.append('netball')
# adds netball to the end of the list

my_list2.insert(2, 'golf')  # inserts new element to the list at specified index

my_list2.pop()  # returns the last element from the list and also removes it from the list

my_list2.remove('handball')  # removes specified element from the list

my_list2.reverse()  # reverses the list

my_list3 = [0, 4, 5, 3, 2, 1, 7, 8, 9, 6]

my_list3.sort()  # sorts elements in the list

new_list3 = sorted(my_list3)  # creates a sorted list while maintaining the original list

# ____________________________________

my_list4 = [10, 20, 30, 40]
my_list5 = [50, 60, 70, 80]
my_list6 = my_list4 + my_list5  # append list4 to list5

a = my_list6[1:5]  # gets elements from index 1 to 5
b = my_list6[:6]  # gets elements from index 0 to 6
c = my_list6[6:]  # gets element from index 6 to end of the list
d = my_list6[::1]  # gets all the elements in the list one after the other
e = my_list6[::2]  # gets elements in the list from index 0 then skipping two steps to get the next element till the end

# ___________________________________________

list_org = [100, 200, 300, 400, 500, 600, 700, 800, 900]

list_copy = list_org  # copies list_org to list_copy. Any change to list_copy affects the list_org

list2_copy = list_org.copy()
list3_copy = list(list_org)
# these two create a new list which is a copy of the list_org
# a change in the copies does not affect the original list

# ____________________________________________________

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [a * a for a in list_a]  #creates a list whose elements are squares of each element in list_a

list_c = [a + a for a in list_a] #creates a list whose elements are sum of each element in list_a

