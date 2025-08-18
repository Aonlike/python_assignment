def is_divisible_by_3_and_5(numbers):
	return numbers % 3 == 0 and numbers % 5 == 0

def divisible_by_3_and_5(numbers):
		return list(filter(is_divisible_by_3_and_5, numbers))

print(divisible_by_3_and_5(range(1, 51)))
	