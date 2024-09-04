from array import array
#LIST
# indexing

#~~~~~~~~~~~ Python Lists ~~~~~~~~~~~~~~~~~~~~~~
names = ["michael", "john", "james", "anne", "freya", "clara"]
#          0,         1        2        3        4         5

second_list = list(["Michael", "John"]) #Use this for large datasets
print(second_list)




user_data = [
    ("mikelove", "apples", 25),
    ("johnnybravo", "bananas", 27),
    ("suzypan", "pears", 21)
]

#user_data.append([("haggie", "runner", 26), ("gunner", "shoot", 18), ("longdistance", "lounge", 22)]) #add item (item[3]) which become a complex list as single item
user_data.extend([("haggie", "runner", 26), ("gunner", "shoot", 18), ("longdistance", "lounge", 22)])
print(user_data)
print(user_data[3])

#~~~~~~~~~~~ List Packing & Unpacking ~~~~~~~~~~~~~~~~~~~~~~

#Packing and Unpacking

age_list = [25,27,21, 22,42,34,18,19]#packed from (packing)

#unpacking...

*users, user4, user5, user6, user7, user8 = age_list
print(user4)

#Complex unpacking 
*main_users, other_user = user_data
print(main_users[0][2]) #2-D (Dimensional) List

#~~~~~~~~~~~ Python Arrays ~~~~~~~~~~~~~~~~~~~~~~

ages_array = array("i", [22,24,27,29, 39,35,44,50])

#1. Using List Comprehension

age_list = [age for age in ages_array]
#print(type(ages_array))
#print(type(ages_list))
#print(ages_list)


#2 List Constructor

ages_list_cons = list(ages_array)
#print(type(ages_list_cons))

#List to Array

ages_empty_array = array("i")
ages_empty_array.fromlist(age_list)
print(ages_empty_array)
print(type(ages_empty_array))
