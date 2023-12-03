#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:parameter>")
def print_string(parameter):
    print('hello')
    return f"{parameter}"

# A count() view should take one parameter
# It should display all numbers in the range of that parameter on separate lines.
#  Its URL should be of the format /count/parameter.
@app.route("/count/<int:parameter>")
def count(parameter):
    count = ""
    for num in range(parameter):
        count = (count + str(num) + "\n")

    return count

# print(count(8))

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == "+":
        return  str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)
    



if __name__ == '__main__':
    app.run(port=5555, debug=True)
