import re


def generate_words(text: str):
    for words in re.findall(r'\b\w+\b', text):
        yield words


if __name__ == '__main__':
    text = 'Мама. Мыла? Маму!'
    for w in generate_words(text):
        print(w)

    assert ['Мама', 'Мыла', 'Раму'] == [i for i in generate_words('Мама. Мыла? Раму!')]
    assert ['Какой', 'прекрасный', 'день'] == [i for i in generate_words('Какой? прекрасный. день!')]
    assert ['Папа', 'тоже', 'мыл', 'раму'] == [i for i in generate_words('Папа, тоже!!!! мыл/ раму?')]
    assert ['И', 'я', 'тоже', 'мыл', 'раму'] == [i for i in generate_words('И. я, тоже!!!!!! мыл: раму}')]