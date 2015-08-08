# Jerricha's!
# Reminder: Make me in Cygwin until Msys environment OK

PROJECT_NAME=Jerrichas

install:
	python setup.py install

run:
	python jerrichas.py

dbshell:
	sqlite3 $$APPDATA/Paragon\ Chat/Database/ParagonChat.db

test-all:
	nosetests -w testing -c etc/test-all.config

test-one:
	nosetests -w testing -c etc/test-one.config

clean:
	find . | grep -E "(__pycache__|\.spec|\.pyc|\.pyo$\)" | xargs rm -rf
	find . | grep -E "(build)" | xargs rm -rf

compile-win:
	make clean
	find . | grep -E "(build|dist)" | xargs rm -rf
	pyinstaller --clean --onefile --icon=docs/jerrichas.ico Jerrichas.py

.PHONY: install clean compile-win test-all test-one run dbshell
