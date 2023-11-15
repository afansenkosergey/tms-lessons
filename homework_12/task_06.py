def generate_words(text: str):
    for words in text.split():
        yield words


if __name__ == '__main__':
    text = 'мама мыла раму'
    for w in generate_words(text):
        print(w)

    assert ['мама', 'мыла', 'раму'] == [i for i in generate_words('мама мыла раму')]
    assert ['Какой', 'прекрасный', 'день'] == [i for i in generate_words('Какой прекрасный день')]
    assert ['Папа', 'тоже', 'мыл', 'раму'] == [i for i in generate_words('Папа тоже мыл раму')]
    assert ['И', 'я', 'тоже', 'мыл', 'раму'] == [i for i in generate_words('И я тоже мыл раму')]