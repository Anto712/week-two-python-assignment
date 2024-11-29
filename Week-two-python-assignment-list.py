#Creating an empty list
my_list = []

#Append element to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1,15)
#extending the list with another list
my_list.extend([50,60,70])
#removing the last element frome my_list
my_list.pop()
#Sorting the my_list in an ascending order
my_list.sort()
#Finding the index of 30 in my_list
index_of_30 = my_list.index(30)

print(f"The index of value 30 is: {index_of_30}")