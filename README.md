# Arabic-Voice-Interface-for-City-Operation-Center

## Online Model Selection 

#### This readme report outlines the process of choosing a model among three alternatives for online speech to text :


### Models :
1. AWS transcribe
2. Google online speech to text
3. Azure speech to text

### Evaluation Criteria:
To determine the most suitable model for the task at hand, the following criteria were taken into account:

**Accuracy**: The ability of the model to provide accurate predictions on the given task using `WER` and `CER`.
**Performance**: The computational efficiency and speed of the model during training and inference.
**Ease of Use**: The simplicity and ease of integration and deployment of the model.


### Dataset Used in evaluation 

We used the dataset given [here](https://drive.google.com/drive/folders/1r313U2MrL9jKmxRA7KJJNl29yl6FLvs6?usp=drive_link) , and for English [here](https://drive.google.com/drive/folders/1OwaTAOHzT4SNE2GdnG6rImX-RO_KbgXg?usp=drive_link).



#### keep in mind the English dataset is not very representative about the actual data but we used some samples created by us and the models seemed to be very good compared to the arabic.* 




### Results



| Model         | WER           | CER   |
| ------------- |:-------------:| -----:|
| Azure		| 0.29		| 0.23  |
| Google        | 0.43          |  0.39 |

#### `AWS transcribe` was eliminated for the following reasons:
1. It requires all the data to be on an S3 bucket 
2. For auto detect the langauge it requires a longer sequences compared to others 
3. Very slow compared to the other two


### Conclusion

After trying the models with different post procesing techinques we came to these results :
* Google speech to text and Azure consume almost the same time.
* Both doesn't do great when there is a pause in the record.


> Based on the previous results of pros and cons we advise to use Azure speech to text


# Progress

* Implemented three online Speech to text models and evaluated them.
* Added Voice Recorder module
* Added Google and azure translator API scripts


 
