from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Just a normal Flask server"

@app.route('/add1/<number>')
def param(number):
    sum = int(number) + 1
    return f"The sum is: {sum}"


if __name__ == "__main__":
    app.run()