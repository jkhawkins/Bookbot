def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_nums(text):
    letter_nums = {}
    text_list = list(text)
    for letter in text_list:
        letter_lower = letter.lower()
        if letter_lower in letter_nums:
            num = letter_nums[letter_lower] + 1
            letter_nums.update({letter_lower: num})
        else:
            letter_nums.update({letter_lower: 1})
    return letter_nums

def sort_on(items):
    return items["num"]

def sort_letters(raw_letters):
    letter_list = []
    for raw_letter in raw_letters:
        if raw_letter.isalpha():
            letter_list.append({"char": raw_letter, "num": raw_letters[raw_letter]})
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

def letter_report(book, words, letter_list):
    bot_header = "============ BOOKBOT ============\n"
    book_text = f"Analyzing book found at {book}...\n"
    wordcount_header = "----------- Word Count ----------\n"
    wordcount_text = f"Found {words} total words\n"
    charcount_header = "--------- Character Count -------\n"
    charcount_text = ""
    for letter in letter_list:
        charcount_text += f"{letter["char"]}: {letter["num"]}\n"
    footer = "============= END ==============="
    total_text = bot_header + book_text + wordcount_header + wordcount_text + charcount_header + charcount_text + footer
    return total_text

