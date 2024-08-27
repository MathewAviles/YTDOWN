from flask import Flask
from flask_cors import CORS 

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

#helloworld
@app.route('/', methods=['GET'])
def hello():
    return("🦈 :3")



@app.route('/downloader', methods=['GET'])
def downloader():
    return("Dowloader medio 🦈")

if __name__ == '__main__':
    app.run(debug=True)
