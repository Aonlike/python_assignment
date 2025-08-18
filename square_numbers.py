def square_number(number):
	return number * number

def square_numbers():
	numbers = range(1,11)
	squared_numbers = list(map(square_number, numbers))
	return squared_numbers

print(square_numbers())


	