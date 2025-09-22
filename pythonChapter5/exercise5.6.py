def rotate(number_0, number_1, number_2):
	return(number_2, number_0, number_1)

a, b, c = 'Doug',22, 1984

a, b, c = rotate(a,b,c)
print("First call: ", a, b, c)

a, b, c = rotate(a,b,c)
print("Second call: ", a, b, c)

a, b, c = rotate(a,b,c)
print("Third call: ", a, b, c)
