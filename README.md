# Arabic-Voice-Interface-for-City-Operation-Center

This repository contains the full code for an Arabic / English  virtual assistant 

# Project Structure

The repository is organized as follows:

data/: This directory contains the dataset used for training and evaluation. It includes both the raw data and preprocessed versions, if applicable.

notebooks/: This directory contains Jupyter notebooks that provide step-by-step explanations of the data exploration, preprocessing, model training, and evaluation processes.

src/: This directory contains the source code for the project, including data preprocessing scripts, model training scripts, and evaluation scripts.

utils/: This directory contains utility functions and helper scripts used throughout the project.

requirements.txt: This file lists the Python libraries and dependencies required to run the code in this repository.

# Getting Started

To get started with the project, follow these steps:

1. Clone the repository : 
    * `git clone https://github.com/Aylore/Arabic-Voice-Interface-for-City-Operation-Center`

2. Install the required dependencies. It is recommended to set up a virtual environment for this project:

    * `cd Arabic-Voice-Interface-for-City-Operation-Center`
    * `make install`


3. Run the project using `Makefile` as follows :
    * Download this pretrained model for the `wav2lip` model<br> `sh get_wav2lip_model.sh`


    * `make rasa-train`  -- **You will need to train `rasa` for the first time only**
    * `make fastapi`
    * `make rasa-run`
    * `make rasa-actions`
    * `make django`

> Make sure to run them in the same order

# Pipeline

1. ## Speech To Text 
    For our first step we needed to take input from the user as audio from the microphone and convert it to text so we used different online services for this like the `google-speech-to-text` and `azure-speech-to-text`.
    for more information check [SST-online](https://github.com/Aylore/Arabic-Voice-Interface-for-City-Operation-Center/tree/STT-online)  branch README


2. ## Rasa-chatbot
    After getting the transcript of the question, Rasa calls an API endpoint to retrieve the answer of the question based on user input language.


3. ## Text To Speech
    After getting the response from our chatbot we had to convert it to audio speech so we used the same services as the first step



4. ## LipSync
    After getting the audio response we had to present the answer to the user in a convenient way so we trained -on an agent of our chosing- a LipSync model using the current SOTA model [wav2lip](https://github.com/Rudrabha/Wav2Lip) , check the [training notebook](notebooks/AE_Expert_Discriminator.ipynb)
    for more information refer to this [branch](https://github.com/Aylore/Arabic-Voice-Interface-for-City-Operation-Center/tree/wav2lip)


5. ## Face restoration
    Due to the output result of the wav2lip model we used an image enhancement model to restore the quality using [Code Former](https://github.com/sczhou/CodeFormer)



6. ## Django-integration
    After all the pipeline were finsihed we integrated it in a django app for ease of use 




# Examples







# Future work
* Edit the face restoration model to use a simpler model for face detection or combining it with wav2lip some how.  *needs further research*
* Taking feedback from the user after receiving his answer to find areas of development and better enhance the pipeline.


# Acknowledgements
1. [wav2lip](https://github.com/Rudrabha/Wav2Lip) ,"A Lip Sync Expert Is All You Need for Speech to Lip Generation In the Wild", published at ACM Multimedia 2020.

2. [code former](https://github.com/sczhou/CodeFormer) ,[NeurIPS 2022] Towards Robust Blind Face Restoration with Codebook Lookup Transformer.