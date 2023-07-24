from flask import Flask
import time

app = Flask(__name__)

print(__name__)

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        print("before hello")
        function()
        print("after hello")
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

say_hello()

@app.route("/")
def hello_world():
    return "Test !"

if __name__ == '__main__':
    app.run()