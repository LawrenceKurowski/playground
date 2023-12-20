from flask import Flask, render_template, request, jsonify
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form',methods=['POST'])
def process_data():
    try:
        # Get the data from the form
        data = request.json
        number_one = data.get('number1')
        number_two = data.get('number2')

        # Process the data (you can perform any backend logic here)
        sum = int(number_one) + int(number_two)

        # Return a JSON response with the processed data
        return jsonify({'message': 'Success', 'result': sum})

    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True)