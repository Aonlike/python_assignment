def add_mango():
	fruits = ('apple', 'banana', 'cherry')
	new_fruits = list(fruits)
	new_fruits.append('mango')
	fruits_list = tuple(new_fruits)
	print(new_fruits)


add_mango()