from flask import Flask, abort, request, session, redirect
from dataclasses import dataclass
import sqlite3
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@dataclass
class Product:
    id: int
    name: str
    description: str
    category_id: int
    favorites_count: int


@dataclass
class Category:
    id: int
    name: str


@dataclass
class User:
    id: int
    login: str
    password: str


def load_products():
    with sqlite3.connect('table_product.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''SELECT id, name, description, category_id, favorites_count 
                            FROM product''')
        rows = cursor.fetchall()
        products = [Product(id=row[0], name=row[1], description=row[2], category_id=row[3], favorites_count=row[4]) for
                    row in rows]
        return products


def load_categories():
    with sqlite3.connect('table_product.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''SELECT id, name 
                            FROM category''')
        rows = cursor.fetchall()
        categories = [Category(id=row[0], name=row[1]) for row in rows]
        return categories


def get_product(product_id) -> Product:
    with sqlite3.connect('table_product.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''SELECT id, name, description, category_id, favorites_count
                       FROM product 
                       WHERE id = ?''', (product_id,))
        row = cursor.fetchone()
        if row is None:
            abort(404, 'PRODUCT NOT FOUND')
        return Product(*row)


def load_product_category(category_name: str) -> list:
    with sqlite3.connect('table_product.db') as conn:
        cur = conn.execute("""SELECT product.id,product.name,product.description,product.category_id,
                        product.favorites_count,category.name
                        FROM category JOIN product
                        on category.id=product.category_id
                        where category.name=?""", (category_name,))
        result = []
        for i in cur.fetchall():
            result.append(Product(id=i[0], name=i[1], description=i[2], category_id=i[3], favorites_count=i[4]))
        category_name = i[5]
        result.append(category_name)
    return result


def get_category(category_name) -> Category:
    with sqlite3.connect('table_product.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''SELECT id, name 
                                FROM category 
                                WHERE name = ?''', (category_name,))
        row = cursor.fetchone()
        if row is None:
            abort(404, 'CATEGORY NOT FOUND')
        return Category(*row)


def save_product(product: Product):
    with sqlite3.connect('table_product.db') as connection:
        cursor = connection.cursor()
        data = (product.name, product.description, product.category_id, product.favorites_count, product.id)
        cursor.execute('''UPDATE product 
                       SET name = ?, description = ?, category_id = ?, favorites_count = ?
                       WHERE id = ?''', data)


def generate_html_list(products: list[Product]) -> str:
    product_html = '\n'.join(
        f'<li><a href="/product/{product.id}">{product.name}</a></li>'
        for product in products)
    return f"""
    <html>
        <head>
            <title>Product List</title>
        </head>
        <body>
            <ul>
                {product_html}
            </ul>
        </body>
    </html>"""


@app.route('/')
@app.route('/products')
def main_page():
    user_nickname = get_user_nickname()
    is_authenticated = 'user_id' in session
    with sqlite3.connect('table_product.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''SELECT p.id as product_id, p.name as product_name, p.description as product_description, 
                                p.category_id, p.favorites_count,
                                c.name as category_name
                          FROM product p
                          JOIN category c ON p.category_id = c.name''')
        rows = cursor.fetchall()

    grouped_products = {}
    for row in rows:
        product = Product(id=row[0], name=row[1], description=row[2], category_id=row[3], favorites_count=row[4])
        category_name = row[5]

        if category_name not in grouped_products:
            grouped_products[category_name] = []
        grouped_products[category_name].append(product)

    category_html = '\n'.join(
        f'<li><a href="/category/{category_name}">{category_name}</a>'
        f'<ul>{generate_html_list(products)}</ul></li>'
        for category_name, products in grouped_products.items()
    )

    return f"""
        <html>
            <head>
                <title>Магазин</title>
            </head>
            <body>
                <h1>Главная страница</h1>
                <div>
                    
                    {'' if is_authenticated else ('<a href="/login">Войти</a> |'
                                                  ' <a href="/registration">Регистрация</a>')}
                    {f"Привет, {user_nickname}!" if user_nickname else ""}
                    {'' if not is_authenticated else '<a href="/logout">Logout</a>'}
                </div>
                <ul>
                    <h3>{category_html}</h3>
                </ul>
            </body>
        </html>
        """


@app.route('/product/<int:product_id>')
def product_detail(product_id: int):
    product = get_product(product_id)
    if product is None:
        abort(404, 'Product not found')
    favorites_product = session.get('favorites_product', set())
    is_favorite = product_id in favorites_product
    return f"""
    <html>
        <head>
            <title>Продукт</title>
        </head>
        <body>
            <a href="/products">Вернуться на главную страницу</a>
            <h1>{product.name}</h1>
            <h3>{product.description}</h3>
            <p><a href="/category/{product.category_id}">Категория: {product.category_id}</a></p>
            <form method="post" action="/product/add_to_favorites">
                <input type="hidden" value="{product.id}" name="product_id"/>
                <input type="submit" value="Add to favorite"/>
                <span class="favorite-star">{'&#10027' if is_favorite else ""}</span>
            </form>
        </body>
    </html>"""


@app.route('/product/add_to_favorites', methods=['POST'])
def add_to_favorites():
    product_id = int(request.form.get('product_id'))
    favorites_product = session.setdefault('favorites_product', set())
    product = get_product(product_id)
    if product_id not in favorites_product:
        product.favorites_count += 1
        favorites_product.add(product_id)
    else:
        product.favorites_count -= 1
        favorites_product.remove(product_id)
    save_product(product)
    return redirect(f'/product/{product.id}')


@app.route('/category/<category_id>')
def category_detail(category_id: int):
    category = get_category(category_id)
    if category is None:
        abort(404, 'Category not found')

    products_in_category = [product for product in load_products() if product.category_id == category.name]

    product_html = '\n'.join(
        f'<li><a href="/product/{product.id}">{product.name}</a></li>'
        for product in products_in_category)

    return f"""
    <html>
        <head>
            <title>Категория</title>
        </head>
        <body>
            <a href="/products">Вернуться на главную страницу</a>
            <h1>Категория: {category.name}</h1>
            <ul>
                {product_html}
            </ul>
        </body>
    </html>
    """


# -------------------Registration------------------------
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        with sqlite3.connect('table_product.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO user (login, password) VALUES (?, ?)', (login, password))
            connection.commit()
        user = get_user(login, password)
        if user:
            session['user_id'] = login
        return redirect('/login')

    return """
    <html>
        <head>
            <title>Регистрация</title>
        </head>
        <body>
            <a href="/products">Вернуться на главную страницу</a>
            <h1>Регистрация</h1>
            <form method="post" action="/registration">
                <label for="login">Логин:</label>
                <input type="text" id="login" name="login" required><br>
                <label for="password">Пароль:</label>
                <input type="password" id="password" name="password" required><br>
                <input type="submit" value="Зарегистрироваться">
            </form>
        </body>
    </html>
    """


def get_user_nickname() -> str:
    user_id = session.get('user_id')
    if user_id:
        with sqlite3.connect('table_product.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT login FROM user WHERE login = ?', (user_id,))
            user = cursor.fetchone()
            return user[0] if user else ""
    return ''


def get_user(login: str, password: str):
    with sqlite3.connect('table_product.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''SELECT *
                                FROM user
                                WHERE login = ? AND password = ?''', (login, password))
        row = cursor.fetchone()
        if row:
            return User(id=row[0], login=row[1], password=row[2])
        return None


@app.route('/authentication', methods=['POST'])
def authentication():
    login = request.form['login']
    password = request.form['password']
    user = get_user(login, password)
    if user:
        session['user_id'] = login
        return redirect('/')
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login_in():
    return (f"""
    <html>
        <head>
            <title>Login</title>
        </head>
        <body>
            <form action="/authentication" method="post">
                <a href="/products">Вернуться на главную страницу</a><br>
                <h1>Авторизация</h1>
                <label for="username">Логин:</label>
                <input type="text" name="login" /><br> 
                <label for="password">Пароль:</label>
                <input type="password" name="password" /><br>
                <input type="submit" value="Войти" />
            </form>
        </body>
    </html>
    """)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(port=8084, debug=True)
