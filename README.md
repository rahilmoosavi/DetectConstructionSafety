# Summary
This is a repository for detecting the use or non-use of mask, safety-vest and hardhat of workers  by applying the YOLO algorithm. The model can be a convenient way to monitor and ensure that workers adhering to safety protocols, such as wearing appropriate personal protective equipment (PPE).
To go along with this repo, I also [wrote an article]( https://medium.com/@rahil.gh.moosavi/how-to-check-construction-safety-with-yolo-model-and-python-language-b4073139c73) that explained the project step by step.
# DetectConstructionSafety
Construction Site Safety is a Computer Vision Project. You can run this project in the following way on your system and on PyCharm or clone this repository on Google Colab with following script.
```
!git clone https://github.com/rahilmoosavi/DetectConstructionSafety.git
cd /content/DetectConstructionSafety
!python ConstructionSafetyVideo.py
```
# Run The Project Step By Step From Scratch
- Step1: Download dataset from the following link [roboflow](https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety)
</br>Note:  you may have to log in to the site to download the dataset.
- Step2: Upload the dataset in your Google Drive then mount it .after that you train a model in Google Colab as below. 
Before running any scripts, make sure to download the correct packages. You can do so by running the following commands.
```
!pip install ultralytics
from ultralytics import YOLO
cd /content
```
```
!yolo task=detect mode=train model=yolov8l.pt data='/content/drive/MyDrive/YoloDataset/Construction Site Safety.v30-raw-images_latestversion.yolov8/data.yaml' epochs=50
```
- Note: The dataset is located in the following path in my Google Drive.
<br>drive/MyDrive/YoloDataset/Construction Site Safety.v30-raw-images_latestversion.yolov8

- Step3: After the model training is done, you can download best.pt from directory look as follows.
 <img src="https://github.com/rahilmoosavi/DetectConstructionSafety/blob/master/Images/path.JPG" width="500">
 
- Step4: Now you can run ConstructionSafetyVideo.py or ConstructionSafetyImage.py to detect ConstructionSafety.

The results are saved as video and image files.

<img src="https://github.com/rahilmoosavi/DetectConstructionSafety/blob/master/newobject.jpg?raw=true" width="500">


https://github.com/rahilmoosavi/DetectConstructionSafety/assets/82846974/15a0db17-0fb3-4de2-9e2e-7b7ed7718751



 







