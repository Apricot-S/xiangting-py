.PHONY: build docs

all: build docs

build:
	uv build && uv sync --reinstall


docs:
	cd docs && make clean html
