from flask import Flask

app = Flask(__name__)


@app.route('/ping')
def ping():
    return f"""
<html>
   <head>
       <title>Pong</title>
   </head>
   <body>
       <a href="/pong">pong</a>
       </form>
   </body>
</html>
"""


@app.route('/pong')
def pong():
    return f"""
    <html>
       <head>
           <title>Ping</title>
       </head>
       <body>
           <a href="/ping">ping</a>
           </form>
       </body>
    </html>
    """


if __name__ == '__main__':
    app.run(port=8081, debug=True)
