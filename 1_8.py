from random import random

list = []
for x in range(50):
	list.append(random())

new_list = []
while list:
	min = list[0]
	for x in list: 
		if x < min:
			min = x
	new_list.append(min)
	list.remove(min)    

print (new_list[::-1])