class WordIterable:

    def __init__(self, text: str):
        self.text = text.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.text):
            result = self.text[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


if __name__ == '__main__':
    for i in WordIterable('мама мыла раму'):
        print(i)

    assert ['мама', 'мыла', 'раму'] == [i for i in WordIterable('мама мыла раму')]
    assert ['пришел', 'новый', 'год'] == [i for i in WordIterable('пришел новый год')]
    assert ['завтра', 'новый', 'день'] == [i for i in WordIterable('завтра новый день')]
    assert (['31', 'декабря', 'заканчивается', 'год', 'и', 'наступает', 'новый']
            == [i for i in WordIterable('31 декабря заканчивается год и наступает новый')])