from flask import Flask, current_app, g, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello sjseo Flask tutorial"

@app.route('/name/<name>',
    methods=["GET", "POST"],
    endpoint="hello-endpoint")

def hello(name):
    return render_template("index.html", name=name)

# ctx = app.app_context()
# ctx.push()

# with app.test_request_context("/user?updated=true"):
#     print(request.args.get("updated"))

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # 임시
        return redirect(url_for("contact_complete"))
    return redirect("contact_complete")
