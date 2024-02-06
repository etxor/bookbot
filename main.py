def main():
    book_path = "books/frankestein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for char in text:
        if not char.isalpha():
            continue
        lower = char.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
    return chars

main()