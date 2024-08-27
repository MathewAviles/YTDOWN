from flask import Flask
from flask_cors import CORS 

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

#helloworld
@app.route('/', methods=['GET'])
def hello():
    return("Hello from Flask!")



@app.route('/downloader', methods=['GET'])
def downloader():
    return("Hello from Flask!2")

if __name__ == '__main__':
    app.run(debug=True)
