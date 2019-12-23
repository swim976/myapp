from flask import Flask
import os


static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app = Flask(__name__, static_folder=static_folder, static_url_path='')


@app.route('/')
def index():
    return "hello world !!!  =翁金科技="


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=9886)
