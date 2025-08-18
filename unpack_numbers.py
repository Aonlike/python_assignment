def unpack_numbers():
	numbers = (10,20,30,40)
	a , b , *other = numbers
	return(a,b, other)


print(unpack_numbers())