def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
   path = get_book_text("books/frankenstein.txt")
   print(f"{path}")

def number_of_words():
    
    print(f"{num_words} words found in the document")


main()