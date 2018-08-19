import yaml
from os import listdir
from markdown2 import markdown

config = {}

with open("config.yml", "r") as f:
    config = yaml.load(f.read())

content_dir = "src/" + config["content_dir"] or "content"
data_dir = "src/" + config["data_dir"] or "data"
templates_dir = "src/" + config["templates_dir"] or "src/templates"
data_files = listdir(data_dir)


def get_templates_folder():
    return templates_dir


def get_data():
    data = {}
    for file in data_files:
        with open(f"{data_dir}/{file}", "r") as f:
            data[file.replace(".yml", "")] = yaml.load(f.read())

    data["site"] = config

    return data


def get_content(files):
    content = {}
    for file in files:
        with open(f"{content_dir}/{file}.md", "r") as main_content:
            content[file] = markdown(main_content.read())

    return content
