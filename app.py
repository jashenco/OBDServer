from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! This will be the OBD Server. Test Push. Watchtower Test.</p>"

if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')