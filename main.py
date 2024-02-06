def main():
    book_path = "books/frankestein.txt"
    text = get_book_text(book_path)
    words_count = count_words(text)
    chars_count = count_chars(text)
    report = get_report(book_path, words_count, chars_count)
    print(report)

def get_book_text(pathname):
    with open(pathname) as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars_dict = get_chars_dict(text)
    chars_list = get_chars_list(chars_dict)
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list 

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

def get_chars_list(chars_dict):
    chars = []
    for char, count in chars_dict.items():
        chars.append({"char": char, "count": count})
    return chars

def sort_on(chars_dict):
    return chars_dict["count"]

def get_report(book_path, words_count, chars_list):
    report = ""
    report += f"---------- Begin report for {book_path} ----------\n"
    report += f"{words_count} words were found in the book.\n"
    for char_dict in chars_list:
        report += get_report_line(char_dict)
        report += "\n"
    report += f"---------- End report for {book_path} ----------\n"
    return report

def get_report_line(char_dict):
    return f"The {char_dict["char"]} character was found {char_dict["count"]} times."

main()