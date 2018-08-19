# paqrat

_currently a work in progress_

A flask site that compiles to static

### Requirements

- python3

### Getting started

- `python3 -m venv venv`
- `. venv/bin/activate`
- `pip install -r requirements.txt`
- `export FLASK_APP=app.py`
- `flask run`

### How it works

Data in `/data` will be associated with the `data` variable in all pages.

Each data file is added to the data `dict` and it's associated filename is added as a key to it's data varaiables

ie: `{{ data.site.title }}` would be associated with `/data/site.yml`

### Content

Basic content entries are under `/content`.

You can pass an array of content files to use in your route template: `get_content(['index, about'])`
This will apply it to the templates `content` variable `{{ content.index }} {{ content.about }}`
This allows for separating content into any markdown file in `/content` and using it in multiple areas and templates.


### Build

`python3 build_static.py`

This will create a build directory with static files ready for deployment.
