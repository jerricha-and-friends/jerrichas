# Jerricha's!
# Reminder: Make me in Cygwin until Msys environment OK

PROJECT_NAME=Jerrichas

install:
	python setup.py install

run:
	python jerrichas.py

test-all:
	nosetests -w testing -c etc/test-all.config

test-one:
	nosetests -w testing -c etc/test-one.config

clean:
	find . | grep -E "(__pycache__|\.spec|\.pyc|\.pyo$\)" | xargs rm -rf
	find . | grep -E "(build|dist)" | xargs rm -rf

compile-win:
	make clean
	# pyinstaller --debug --onefile Jerrichas.py
	# pyinstaller --clean --onefile Jerrichas.py
	pyinstaller --clean --onefile --icon=docs/jerrichas.ico Jerrichas.py

.PHONY: install clean compile-win test-all test-one run
