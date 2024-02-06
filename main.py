def main():
    book_path = "books/frankestein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(num_words)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

main()