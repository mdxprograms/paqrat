import yaml
from os import listdir
from markdown2 import markdown


content_dir = "content"
data_dir = "data"
data_files = listdir(data_dir)


def get_data():
    data = {}
    for file in data_files:
        with open(f"{data_dir}/{file}", "r") as f:
            data[file.replace(".yml", "")] = yaml.load(f.read())

    return data


def get_content(files):
    content = {}
    for file in files:
        with open(f"{content_dir}/{file}.md", "r") as main_content:
            content[file] = markdown(main_content.read())

    return content
