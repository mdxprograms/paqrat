from os import getcwd, listdir
import yaml
from flask import Flask, Markup, render_template
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
