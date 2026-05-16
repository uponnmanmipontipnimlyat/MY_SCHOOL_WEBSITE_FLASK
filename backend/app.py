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

@app.route('/hello')
def hello():
    name = request.args.get("name", "flask")
    return f"<h1>Hello World, Welcome to my flask App, my name is, {escape(name)}!</h1>"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>/')   
def show_post(post_id):
    return f'post_id {escape(post_id)}'

@app.route('/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

if __name__ == '__main__':
    app.run(debug=True)
