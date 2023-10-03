def get_longest_word(words: str) -> str:
    return max(words.split(), key=len)


assert get_longest_word("hello this is a string with words and spaces and big big woooooooooord") == 'woooooooooord'
assert get_longest_word('A long sentence of random letters is complex without being specified')  == 'specified'