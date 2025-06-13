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

def sorted_list(char_count):
    sorted = []
    for count in char_count:
        if count.isalpha():
            num = char_count[count]
            dict = {"char": count, "num": num}
            sorted.append(dict)
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def sort_on(dict):
    return dict["num"]

    






