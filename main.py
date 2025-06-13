from stats import (
    get_number_of_words, 
    book_char_count, 
    sorted_list
)


def main():
   book_path = "books/frankenstein.txt"
   text = get_book_text(book_path)
   num_words = get_number_of_words(text)
   character_count = book_char_count(text)
   character_count_sorted = sorted_list(character_count)
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

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()