def get_most_frequent_word(text: str) -> str:
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    max_count = 0
    most_frequent_word = ""
    for word, count in word_counts.items():
        if count > max_count:
            max_count = count
            most_frequent_word = word

    return most_frequent_word


assert get_most_frequent_word("hello this is a string with words and spaces and big big woooooooooord and and and") == 'and'
