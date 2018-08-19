from flask import Flask, render_template
from lib.configure import get_templates_folder, get_content, get_data

app = Flask(__name__, template_folder=get_templates_folder())


@app.route("/")
def index():
    return render_template("index.html",
                           content=get_content(["index"]),
                           data=get_data())


@app.route("/about/")
def about():
    return render_template("about.html",
                           content=get_content(["about"]),
                           data=get_data())


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", data=get_data()), 404
