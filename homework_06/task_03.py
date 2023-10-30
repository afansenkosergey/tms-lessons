def remove_vowels(letters):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return list(filter(lambda letter: letter.lower() not in vowels, letters))


user_input = input("Enter the letters: ")
letters_input = user_input.split()

result = remove_vowels(letters_input)
result = [letter.lower() if letter.islower() else letter.upper() for letter in result]

print(result)
