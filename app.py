from flask import Flask
import lib.configure as paqrat

app = Flask(__name__,
            template_folder=paqrat.get_templates_folder(),
            static_folder=paqrat.get_static_folder())


@app.route("/")
def index():
    return paqrat.render("index.html", paqrat.get_content(["index"]))


@app.route("/about/")
def about():
    return paqrat.render("about.html", paqrat.get_content(["about"]))


@app.errorhandler(404)
def page_not_found(e):
    return paqrat.render("404.html"), 404
