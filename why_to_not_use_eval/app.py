from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Just a normal Flask server"

@app.route('/add1/<number>')
def param(number):
    sum = eval(number) + 1 #dangerous implementation!
    #sum = int(number) + 1 #safer implementation. 
    return f"The sum is: {sum}"


if __name__ == "__main__":
    app.run()
