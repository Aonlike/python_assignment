def is_palindrome_word(word):
	return word == word[::-1]

def is_palindrome():
	words = ['level', 'world', 'madam', 'python']
	palindrome = list(filter(is_palindrome_word, words))
	return palindrome

print(is_palindrome())

