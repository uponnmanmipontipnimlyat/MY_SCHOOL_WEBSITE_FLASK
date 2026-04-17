from flask import Flask, jsonify
from flask import request
from markupsafe import escape
app  = Flask(__name__)
@app.route('/')
def home():
    return "Hello, World!"

@app.route('/greetings')
def greetings():
    return '<h1>Welcome to the Flask App!</h1>'

@app.route('/greet-user/<username>')
def greet_user(username):
    """Return a JSON greeting for the provided username."""
    return jsonify({
        "message": f"Hello, {username}!",
        "status": "success"
    })



@app.route("/hi")
def hi():
    name = request.args.get("name", "Flask")
    return f"Hi, {escape(name)}!"
if __name__ == '__main__':
    app.run(debug=True)
