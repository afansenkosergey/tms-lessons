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
