def is_palindrome(string):
	length = len(string)
	for count in range(0, length // 2):
		if(string[count] != string[length - count - 1]):
			return False
	
	return True

string1 = "radar"
print(is_palindrome(string1))

string1 = "moon"
print(is_palindrome(string1))



		
	