install:
	pip install -r requirements.txt

fastapi:
	uvicorn utils.fastapi:app

rasa-run:
	cd src/rasa && rasa run --enable-api

rasa-actions:
	cd src/rasa && rasa run actions

rasa-train:
	cd src/rasa && rasa train

django:
	cd interface && python manage.py runserver 7000