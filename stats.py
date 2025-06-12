def get_number_of_words(text):
    words = text.split()
    return len(words)

def book_char_count(text):
    char_count = {}
    lowercase_version = text.lower()
    characters = list(lowercase_version)
    for char in characters:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count




