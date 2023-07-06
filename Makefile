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

rasa-chat:
	cd src/rasa && python rasamodel.py

# You may encounter HTTP ERROR 403 in order to solve it, you can try using this command `kill $(lsof -t -i:7000)`
django:
	cd interface && python manage.py runserver 7000

wav2lip-model:
	wget "https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/download.aspx?share=EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA" -O "src/wav2lip/checkpoints/wav2lip_gan.pth"