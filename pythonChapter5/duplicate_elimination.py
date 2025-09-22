def duplicate_elimination(values):
	unique_values = []
	for value in values:
		if value not in unique_values:
			unique_values.append(value)
	unique_values.sort()
	return unique_values

numbers = [7, 8, 9,10,7,8,2,7,1,2,4,3,3,5,4]
sort_numbers = duplicate_elimination(numbers)
print(sort_numbers)