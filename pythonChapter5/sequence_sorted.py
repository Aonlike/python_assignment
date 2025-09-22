def is_ordered(sequence):
	for number in range(len(sequence) - 1):
		if sequence[number] > sequence[number + 1]:
			return True

	return False


print( is_ordered([4,5, 1,3,4,5]))
print( is_ordered([1, 2, 3, 4, 5]))

print( is_ordered((5,10,15,20,25)))
print( is_ordered((6,2,3,4,7,8)))


print( is_ordered("rstuv"))
print( is_ordered("strvu"))











	
