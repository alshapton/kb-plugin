.PHONY: default, lint

default:
	python -m kb
spell:
	codespell . --ignore-words-list=hist --skip=./.* --quiet-level=2 || true
lint:
	pylint kb-plugin
pep8:
	autopep8 kb-plugin --in-place --recursive --aggressive --aggressive
clean:
	rm -rf build/ dist/ kb_plugin.egg-info/
test:
	codespell . --ignore-words-list=hist --quiet-level=2
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	pytest
reinstall:
	pip uninstall kb-plugin
	pyenv rehash
	pip install .
	pyenv rehash
