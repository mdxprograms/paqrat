from flask import Flask, render_template
import lib.configure as paqrat

app = Flask(__name__, template_folder=paqrat.get_templates_folder())
data = paqrat.get_data()

@app.route("/")
def index():
    return render_template("index.html",
                           content=paqrat.get_content(["index"]),
                           data=data)


@app.route("/about/")
def about():
    return render_template("about.html",
                           content=paqrat.get_content(["about"]),
                           data=data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", data=data), 404
