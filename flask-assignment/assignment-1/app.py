from flask import Flask

app = Flask(__name__)


@app.route('/api')
def hello_world():
    with open('data.json', 'r') as file:
        data = file.read()
    return data
        

if __name__ == '__main__':
    app.run(debug=True)