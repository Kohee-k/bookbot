def main():
   book_path = "books/frankenstein.txt"
   text = get_book_text(book_path)
   print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_of_words():
    num_words = 0
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    for word in words:
        num_words += 1
    return num_words



main()