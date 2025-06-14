import sys

from stats import (
    get_number_of_words, 
    book_char_count, 
    sorted_list
)

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
   book_path = sys.argv[1]
   text = get_book_text(book_path)
   num_words = get_number_of_words(text)
   character_count = book_char_count(text)
   character_count_sorted = sorted_list(character_count)
   print_report(book_path, num_words, character_count_sorted)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(book_path, num_words, character_count_sorted):
   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {book_path}...")
   print("----------- Word Count ----------")
   print(f"Found {num_words} total words")
   print("--------- Character Count -------")
   for char_dict in character_count_sorted:
       num = char_dict["num"]
       char = char_dict["char"]
       print(f"{char}: {num}")
   print("============= END ===============")


main()