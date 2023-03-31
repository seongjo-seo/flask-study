from flask import Flask, render_template, url_for, current_app, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello sjseo Flask tutorial"

@app.route('/name/<name>',
    methods=["GET", "POST"],
    endpoint="hello-endpoint")

def hello(name):
    return render_template("index.html", name=name)



ctx = app.app_context()
ctx.push()

with app.test_request_context("/user?updated=true"):
    print(request.args.get("updated"))

