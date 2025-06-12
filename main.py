def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
"""
def main():
   path = get_book_text("books/frankenstein.txt")
   print(f"{path}")
"""
def main():
    num_words = 0
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    for word in words:
        num_words += 1
    print(f"{num_words} words found in the document")


main()