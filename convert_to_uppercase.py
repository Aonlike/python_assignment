def convert_to_uppercase():
	languages = ['python', 'java', 'c++']
	uppercase_languages = list(map(str.upper, languages))
	return uppercase_languages


print(convert_to_uppercase())

