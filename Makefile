.PHONY: build

install:
	echo "Installing packages from requirements.txt"
	./venv/bin/pip3 install -r requirements.txt

dev:
	echo "Running dev server"
	FLASK_APP=app.py FLASK_ENV=development flask run

build:
	rm -rf ./build
	./venv/bin/python3 ./build_static.py
