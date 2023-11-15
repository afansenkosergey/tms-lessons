import re


class WordIterable:

    def __init__(self, text: str):
        self.text = re.findall(r'\b\w+\b', text)
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
    for i in WordIterable('Мама. Мыла? Раму!'):
        print(i)

    assert ['Мама', 'Мыла', 'Раму'] == [i for i in WordIterable('Мама. Мыла? Раму!')]
    assert ['Пришел', 'новый', 'год'] == [i for i in WordIterable('Пришел/ новый: год!')]
    assert ['Завтра', 'новый', 'день'] == [i for i in WordIterable('Завтра! новый, день?')]
    assert (['31', 'декабря', 'заканчивается', 'год', 'и', 'наступает', 'новый']
            == [i for i in WordIterable('31/ декабря. заканчивается! год? и, наступает. новый?')])