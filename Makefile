
install:
	pip install -r requirements.txt

fastapi:
	uvicorn utils.fastapi:app

rasa-run:
	rasa run --enable-api

rasa-actions:
	cd src/rasa && rasa run actions

django:
	python interface/manage.py runserver 7000