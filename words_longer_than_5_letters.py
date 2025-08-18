def is_words_longer_than_5(word):
    return len(word) > 5
def words_longer_than_5_letters():
    words = ['cat', 'elephant', 'tiger', 'lion', 'Python']
    return list(filter(is_words_longer_than_5, words))

print(words_longer_than_5_letters())
