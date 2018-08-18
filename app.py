from os import getcwd, listdir
import yaml
from flask import Flask, render_template
from markdown2 import markdown
app = Flask(__name__)

content_dir = "./content"
data_files = listdir("./data")

data = {}
for file in data_files:
    with open(f"{getcwd()}/data/{file}", "r") as f:
        data[file.replace(".yml", "")] = yaml.load(f)


@app.route("/")
def index():
    with open(f"./{content_dir}/index.md", "r") as main_content:
        content = markdown(main_content.read())

    return render_template("index.html", content=content, data=data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", data=data), 404
