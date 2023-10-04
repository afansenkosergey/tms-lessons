def remove_vowels(letters):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return list(filter(lambda x: x not in vowels, letters))


user_input = input("Enter the letters: ").lower()
letters = user_input.split()
print(remove_vowels(letters))