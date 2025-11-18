import sys
from stats import get_num_words, get_letter_nums, sort_letters, letter_report

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    try:
        book = sys.argv[1]
        num_words = get_num_words(get_book_text(book))
        letter_nums = get_letter_nums(get_book_text(book))
        report = letter_report(book, num_words, sort_letters(letter_nums))
        print(report)
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()