from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_function', methods=['POST'])
def execute_function():
    # This function will be called when the frontend button is clicked
    # You can put your backend logic here
    print("Function executed!")
    return "Function executed!"

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/backend-endpoint', methods=['POST'])
def execute_function():
    # This function will be called when the frontend button is clicked
    # You can put your backend logic here
    
    user_input = request.json.get('enteredNumber')

    return jsonify({'result': user_input})

if __name__ == '__main__':
    app.run(debug=True)