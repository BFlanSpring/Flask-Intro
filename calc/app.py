from flask import Flask, request
app = Flask (__name__)

# @app.route ("/add")
# def addition():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = a + b
#     return str(result)

# @app.route ("/subtract")
# def subtraction():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = a - b
#     return str(result)

# @app.route ("/times")
# def multiplication():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = a * b
#     return str(result)

# @app.route("/divide")
# def division():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     result = a / b
#     return str(result)

math_operations = {
    'add': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mult': lambda a, b: a * b,
    'div': lambda a, b: a / b
}

@app.route("/math/<operation>")
def math_operation(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    if operation in math_operations:
        result = math_operations[operation](a, b)
        return str(result)
    else:
        return "Invalid operation"

if __name__ == '__main__':
    app.run()