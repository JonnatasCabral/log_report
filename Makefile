export_log:
	python export_quake_log.py
summary:
	@python reports.py
run:
	@FLASK_APP=./app.py flask run

requirements:
	@pip install -r requirements.txt

test: 
	@python -m unittest
setup: requirements



