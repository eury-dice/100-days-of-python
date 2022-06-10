from flask import Flask, render_template
import requests

BLOGS_API = "https://api.npoint.io/5abcca6f4e39b4955965"

app = Flask(__name__)

blogs = requests.get(BLOGS_API).json()


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    post = blogs[post_id - 1]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
