# Arabic-Voice-Interface-for-City-Operation-Center

## Wav2Lip 
this branch have the code for the implementation of wav2lip model in our project




## you need to download the following models to their corresponding locations

1. wav2lip model to **src/wav2lip/models** <br>  

    `!wget 'https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/download.aspx?share=EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA' -O 'src/wav2lip/checkpoints/wav2lip_gan.pth`


2. <s>face detection model to **src/wav2lip/face_detection/detection/sfd** </s> <br> 

    <s>`!wget "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth" -O "src/wav2lip/face_detection/detection/sfd/s3fd.pth"` </s>





# Data Acquisition 
This model requires was trained on the [lrs2 dataset](https://www.robots.ox.ac.uk/~vgg/data/lip_reading/lrs2.html) , but our goal was to finetune it and overfit the model on a specific agent of our choice .

* The agent recorded several videos of herself speaking to the camera , this step was done twice once on Arabic speech and once on English


# Data preprocessing
the processing script required for the training data is found on the original [wav2lip repo](https://github.com/Rudrabha/Wav2Lip)

### To get the data from its raw form and ready for the processing script the following was done :
* The original videos frame rate were changed to 25 fps to follow the recommended bt the original repo
* The videos were cropped to ~5 seconds long videos and named in 5 digits number format -*refer to wav2lip repo to find the structure*-
* Now we ran the preprocessing script that converts the videos to frames and audio file


# Fine-tune Wav2Lip
We ran the training script as found on the original repo with the following changes in hyperparameters:
*   Batch_size : 32
*   num_workers : 1
*   checkpoint_interval : 300 / 500
*   eval_interval : 300 / 500

**Note that you might want to change the hyperparameters according to the capacity of your machine**


Training loss history for the discriminator:
[expert_loss](expert_log)



# Results 
As the authors said `"You might not get good results by training/fine-tuning on a few minutes of a single speaker. This is a separate research problem, to which we do not have a solution yet. Thus, we would most likely not be able to resolve your issue.
"`

so we used the pretrained model which provided decent results


# References
- [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) - This project is based on the work from the original repository by [Prajwal, K R and Mukhopadhyay, Rudrabha and Namboodiri, Vinay P. and Jawahar, C.V]