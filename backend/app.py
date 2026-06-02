from flask import Flask

from flask import request
from markupsafe import escape
from flask import url_for
app  = Flask(__name__)
@app.route('/')
def home():
    return f"""
    <h1>Welcome to my flask App, this is the home page</h1>  <img src={url_for('static', filename='download.jpg')} alt='hello' >
    """
   



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
