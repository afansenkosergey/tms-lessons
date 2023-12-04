from dataclasses import dataclass
import sqlite3


@dataclass
class Article:
    id: int
    title: str
    text: str
    author: str


def get_all_articles() -> list[Article]:
    with sqlite3.connect('database_article.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT id, title, text, author FROM aricle')
        result = cursor.fetchall()
        result = [Article(*values) for values in result]
        return result


def get_article(article_id: int) -> Article:
    with sqlite3.connect('database_article.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT id, title, text, author '
                       'FROM article '
                       'WHERE id = ?', (article_id,))
        result = cursor.fetchall()
        if len(result) != 1:
            raise ValueError
        return Article(*result[0])


def save_article(article: Article):
    with sqlite3.connect('database_article.db') as connection:
        cursor = connection.cursor()
        data = (article.title, article.text, article.author, article.id)
        cursor.execute('UPDATE article '
                       'SET title = ?, text = ?, author = ?'
                       'WHERE id = ?', data)
