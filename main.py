from stats import get_num_words, get_letter_nums

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    letter_nums = get_letter_nums(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")
    print(letter_nums)

main()