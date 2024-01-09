from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  title = "Python Operations with Flask Routing and Views"
  return f'<h1>{title}</h1>'

@app.route('/print/<string:param>')
def print_string(param):
  print(f'print in console: {param}')
  print (param)
  return param


@app.route('/count/<int:integer>')
def count(integer):
  count = f""
  for i in range(integer):
    count += f'{i}\n'
  return count

@app.route('/math/<float:num1><string:operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero!'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation!'

    return f'<h2>Result: {result}</h2>'

if __name__ == '__main__':
    app.run(debug=True)