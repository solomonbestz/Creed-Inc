from flask import Flask, redirect, url_for, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "davidheroku05@gmail.com"
app.config["MAIL_PASSWORD"] = "surajbilly"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"]= True


mail = Mail(app)

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/course")
def course():
    return render_template("course.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        msg = Message(subject=f"Mail from {name}", body=f"Name: {name}\nE-Mail: {email}\nPhone: {phone}\n\n\n{message}", sender="davidheroku05@gmail.com", recipients=["davidheroku05@gmail.com"])
        mail.send(msg)
        return redirect("/")
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)