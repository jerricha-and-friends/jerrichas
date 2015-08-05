# Jerricha's!

PROJECT_NAME=jerrichas

install:
	python setup.py install

test:
	echo "nose test"

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

compile-win:
	pyinstaller --debug --onefile Jerrichas.py

.PHONY: install clean compile-win test
