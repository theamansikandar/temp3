from flask import Flask, jsonify, request

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

@app.route('/')
def menu():
    return jsonify({
        "status": "online",
        "available_operations": ["add", "subtract"]
    })

@app.route('/add', methods=['GET'])
def calculate_add():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({"operation": "addition", "result": add(a, b)})

@app.route('/subtract', methods=['GET'])
def calculate_subtract():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({"operation": "subtraction", "result": subtract(a, b)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)