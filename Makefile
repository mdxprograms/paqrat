.PHONY: build

setup:
	echo "Running initial setup"
	python3 -m venv venv
	. ./venv/bin/activate
	./venv/bin/pip3 install -r requirements.txt

dev:
	. ./venv/bin/activate; \
	./venv/bin/pip3 install -r requirements.txt; \
	FLASK_APP=app.py FLASK_ENV=development flask run; \

build:
	rm -rf ./build
	./venv/bin/python3 ./lib/build_static.py

build_prod:
	rm -rf ./build
	python3 ./lib/build_static.py
