from flask import Flask, current_app, g, render_template, request, url_for, redirect, flash
from email_validator import validate_email, EmailNotValidError

from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

MY_SECRET_KEY = os.getenv("MY_SECRET_KEY")
app.config["SECRET_KEY"] = MY_SECRET_KEY

@app.route('/')
def index():
    return "Hello sjseo Flask tutorial"

@app.route('/name/<name>',
    methods=["GET", "POST"],
    endpoint="hello-endpoint")

def hello(name):
    return render_template("index.html", name=name)

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        is_valid = True

        if not username:
            flash("사용자명은 필수입니다.")
            is_valid = False

        if not email:
            flash("메일 주소는 필수입니다.")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("메일 주소의 형식으로 입력해 주세요.")
            is_valid = False

        if not description:
            flash("문의 내용은 필수입니다.")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        flash("문의해 주셔서 감사드립니다.")
        # contact_complete.html 템플릿에 전달할 데이터 설정

        context = {"message": "문의 완료"}
        return render_template("contact_complete.html", **context)
    return redirect(url_for("contact"))
