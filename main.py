def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_number_of_words():
    num_words = 0
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    for word in words:
        num_words += 1
    return num_words

def main():
   number_words = get_number_of_words()
   print(f"{number_words} words found in the document")




main()