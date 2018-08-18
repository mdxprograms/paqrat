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

Basic content entries for each page are under `/content`.

Content files fall in the same pattern as their associated templates.

If your template is `templates/index.html` then your content would be in
`content/index.md`.

_or_ `templates/about.html` would use `content/about.md` etc...
