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