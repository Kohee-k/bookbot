def main():
   book_path = "books/frankenstein.txt"
   text = get_book_text(book_path)
   num_words = get_number_of_words(text)
   character_count = sorted_list()
   print(f"{num_words} words found in the document")
   print(character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import get_number_of_words, sorted_list

main()