input_string = input ('Enter the elements in the list seperated by spaces ')
print("\n")

user_list = input_string.split()

print ('list: ',user_list)

print("\n")

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

print ('Converted List : ',user_list)

print("\n")

add_element = input ('Enter the new elements to be added in the end of the list ')
new_list = add_element.split()

print("\n")

print ('New Elements : ', new_list)

print("\n")

user_list += new_list

#print ('New Updated List in string format : ',user_list1)

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

print ('New Converted List : ',user_list)

print("\n")


