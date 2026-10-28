from flask import Flask

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

@app.route('/')
def home():
    return "Calculator API: Push 2 (All Operations)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)