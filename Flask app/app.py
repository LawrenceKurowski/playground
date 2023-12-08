from flask import Flask, render_template, request, jsonify
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')







# @app.route('/process_form', methods=['POST'])
# def process_form():
#     try:
#         data= request.get_json()
#         num1=float(data.get('number1'))
#         num2=float(data.get('number2'))
#         result = num1+num2

#         return jsonify({'result':result})
#     except (ValueError,TypeError):
#         return jsonify({'error': 'Invalid input. Please enter valid numbers.'}), 400

if __name__ == '__main__':
    app.run(debug=True)