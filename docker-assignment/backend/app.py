from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def health():
    return "Welcome to the Flask API!"

@app.route('/form', methods=['POST'])
def home():
    body = request.get_json()
    if not body:
        return "No data provided", 400
    # Process the data here (e.g., save to database, perform calculations, etc.)
    return "Data received successfully", 200
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)