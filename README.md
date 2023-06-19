# Arabic-Voice-Interface-for-City-Operation-Center


## you need to download the following models to their corresponding locations

1. wav2lip model to **src/wav2lip/models** <br>  

`!wget 'https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/download.aspx?share=EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA' -O 'src/wav2lip/checkpoints/wav2lip_gan.pth`


2. face detection model to **src/wav2lip/face_detection/detection/sfd**<br>

`!wget "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth" -O "src/wav2lip/face_detection/detection/sfd/s3fd.pth"`