# Jerricha's!
# Reminder: Run me in Cygwin until Msys environment OK

PROJECT_NAME=jerrichas

install:
	python setup.py install

test:
	echo "nose test"

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
	find . | grep -E "(build|dist)" | xargs rm -rf

compile-win:
	find . | grep -E "(build|dist)" | xargs rm -rf
	# pyinstaller --debug --onefile Jerrichas.py
	# pyinstaller --onefile --icon=docs/FILE.ico Jerrichas.py
	pyinstaller --onefile Jerrichas.py

.PHONY: install clean compile-win test
