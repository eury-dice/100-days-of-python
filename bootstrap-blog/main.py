from flask import Flask, render_template, request
import requests
import smtplib
from os import environ

HOST = environ["HOST"]
PORT = environ["PORT"]
RECEIVER = environ["RECEIVER"]
SENDER = environ["SENDER"]
PASS = environ["PASSWORD"]
BLOG_URL = environ["BLOG_URL"]


app = Flask(__name__)

posts = requests.get(url=BLOG_URL).json()


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", message="Contact Me")
    else:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        with smtplib.SMTP(HOST, PORT) as connection:
            connection.starttls()
            connection.login(SENDER, PASS)
            connection.sendmail(from_addr=SENDER,
                                to_addrs=RECEIVER,
                                msg=f"From: {SENDER}\n"
                                    f"To: {RECEIVER}\n"
                                    f"Subject: New Message from Blog\n\n"
                                    f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
                                )

        return render_template("contact.html", message="Successfully sent your message")


@app.route("/post/<int:post_id>")
def get_post(post_id):
    post = posts[post_id - 1]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
