# **Arabic-Voice-Interface-for-City-Operation-Center**

## **Table of Contents**
1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Getting Started](#getting-started)
4. [Pipeline](#pipeline)
    1. [Speech to Text](#speech-to-text)
    2. [Rasa Chatbot](#rasa-chatbot)
    3. [Text to Speech](#text-to-speech)
    4. [LipSync](#lipsync)
    5. [Face Restoration](#face-restoration)
    6. [Django Integration](#django-integration)
5. [Running The Pipeline](#running-the-pipeline)
6. [Examples](#examples)
7. [Team Members](#team-members)
8. [Contributing](#contributing)
9. [Acknowledgments](#acknowledgements)


## **Introduction**
This repository contains the full code for an Arabic & English virtual assistant 

> **It was developed as a final graduation project for ITI Intake 43 AI Mansoura Branch in July 2023 Under the supervision of [Giza Systems](https://gizasystems.com/).**


## **Project Structure**
```
├── Interface
│   ├── google_app
│   ├── interface
├── data
├── notebooks
├── src
│   ├── rasa
│   ├── speechtotext
│   ├── texttospeech
│   ├── translation
│   └── wav2lip
└── utils
```

The repository is organized as follows:

- **Interface/:** This directory is the django project and contains `google_app` as the django app.  

- **data/:** This directory contains the dataset used for training and evaluation. It includes both the raw data and preprocessed versions, if applicable.

- **notebooks/:** This directory contains Jupyter notebooks that provide step-by-step explanations of the data exploration, preprocessing, model training, and evaluation processes.

- **src/:** This directory contains the source code for the project, including data preprocessing scripts, model training scripts, and evaluation scripts.

- **utils/:** This directory contains utility functions and helper scripts used throughout the project.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository: 
   ```
   git clone https://github.com/Aylore/Arabic-Voice-Interface-for-City-Operation-Center
   ```
2. Change directory into the repository:
   ```
   cd Arabic-Voice-Interface-for-City-Operation-Center
   ```

3. Install the **required** dependencies. It is recommended to set up a virtual environment for this project:
     ```
     make install
     ```

  > You will only need to do this for your first time (feel free to use your own)
    
1. Download this pretrained model for the `wav2lip` model using 
   ```
   make wav2lip-model
   ```
2. Train rasa chatbot using 
   ```
   make rasa-train
   ```

## **Pipeline**


1. ### Speech To Text

    The first step of the pipeline is to transcribe the user's spoken question into text using a speech-to-text system. We use the **Azure Speech Services API** to perform this task,
    for more information check [SST-online](https://github.com/Ayloretree/STT-online)  branch README, where we compare between speech-to-text services including **AWS** and **Google Cloud**.

2. ### Rasa-chatbot

    After getting the transcript of the question, The chatbot generates a response to the user's question based on the intent and entities identified in the question. it calls an API endpoint to retrieve the answer.


3. ### Text To Speech
    After getting the response from our chatbot We then use the Azure Speech SDK to synthesize the response into an audio file. The audio file can be played back to the user as the chatbot's spoken response.


4. ### LipSync
    After getting the audio response we had to present the answer to the user in a convenient way so we trained -on an agent of our chosing- a LipSync model using the current SOTA model [wav2lip](https://github.com/Rudrabha/Wav2Lip)
    for more information refer to this [branch](https://github.com/Ayloretree/wav2lip)


5. ### Face Restoration
    Due to the output result of the wav2lip model we used an image enhancement model to restore the quality using [Code Former](https://github.com/sczhou/CodeFormer)


6. ### Django Integration
   After the video response is generated, we send the response to a Django web application. The Django application can then display the video response to the user, along with any additional information or functionality needed.

## **Running The Pipeline**
1. Run the uvicorn server of fastapi
   ``` 
   make fastapi
   ```
2. Activate the rasa api.
   ``` 
   make rasa-run
   ```
3. Run rasa actions to get the data from the api.
   ``` 
   make rasa-actions
   ```
4. Run the django server to use the interface.
   ``` 
   make django
   ```


## **Examples**






## **Team Members**

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>LinkedIn</th>
      <th>GitHub</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ahmed Elghitany</td>
      <td align="center">
        <a href="https://eg.linkedin.com/in/ahmed-elghitany">
          <img src="https://i.stack.imgur.com/gVE0j.png">
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/Aylore/">
          <img src="https://i.stack.imgur.com/tskMh.png">
        </a>
      </td>
    </tr>
    <tr>
      <td>Israa Okil</td>
      <td align="center">
        <a href="https://eg.linkedin.com/in/israa-okil">
          <img src="https://i.stack.imgur.com/gVE0j.png">
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/esraaokil">
          <img src="https://i.stack.imgur.com/tskMh.png">
        </a>
      </td>
    </tr>
    <tr>
      <td>Khaled Ehab</td>
      <td align="center">
        <a href="https://www.linkedin.com/in/aleedo/">
          <img src="https://i.stack.imgur.com/gVE0j.png">
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/Aleedo">
          <img src="https://i.stack.imgur.com/tskMh.png">
        </a>
      </td>
    </tr>
    <tr>
      <td>Osama Oun</td>
      <td align="center">
        <a href="https://eg.linkedin.com/in/osama-fayez">
          <img src="https://i.stack.imgur.com/gVE0j.png">
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/osamaoun97">
          <img src="https://i.stack.imgur.com/tskMh.png">
        </a>
      </td>
    </tr>
  </tbody>
</table>


## **Contributing**
If you would like to contribute to this project, Feel Free to make a pull request or contact one of our team members via the links above. 


## **Acknowledgements**
1. [wav2lip](https://github.com/Rudrabha/Wav2Lip), "A Lip Sync Expert Is All You Need for Speech to Lip Generation In the Wild", published at ACM Multimedia 2020.

2. [Code Former](https://github.com/sczhou/CodeFormer), [NeurIPS 2022] Towards Robust Blind Face Restoration with Codebook Lookup Transformer.

[def]: #project-structure