def create_anagrams(word):
	anagrams = []
	for letter in range(len(word)):
		first_letter = word[letter]
		rest = word[:letter] + word[letter+1:]
		for sub_anagram in create_anagrams(rest):
			anagrams.append(first_letter)
	return anagrams


word = "Fallen"
all_anagrams = create_anagrams(word)
unique_anagrams = sorted(set(all_anagrams))
print("Anagrams of", word, "are:")
for a in unique_anagrams:
	print(a)
	