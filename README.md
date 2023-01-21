# Hand-Gestures-Recongnition with ResNet50 used for controlling SCARA Robotic Arm.

Hand gestures detection using Tensorflow, Keras and pre-trained model ResNet50 then applying the final output on real-time application.

 ![](https://github.com/Muhameddemadd/Hand-Gestures-Recognition/blob/master/Readme_imgs/IMG-2319.gif)


## Introduction
Snap your fingers and make your coffee maker brew you a fresh cup. Wave a hand near your smart TV and switch on your favorite show. Drag your hand down and drop down the curtains. Grab your hand fist to turn off the lights. How great would it be to get things done just by gesturing? It’s not that unrealistic anymore: hand tracking and gesture recognition technologies are penetrating multiple industries. But do we really need capabilities like these? In this project we will discover how to build a Hand Gestures Recognition model then apply it to a real-time application.

When it comes to real-time AI applications, Processing time and accuracy mean alot. So it’s preferred to try many approaches then choosing the best of them to get the desired results.
 
The approaches I went through to control the robotic arm using the hand:
* The position of the hand on the pixel grid.
* Trained model to classify the different hand gestures.


## Getting Started
### Prerequisites
* Python 3.6 or Higher
* TensorFlow 2.x
* OpenCV
* Numpy
* Mediapipe

### Installation
```
pip install -r requirements.txt
```

## Dataset
### The dataset is manually collected with mediapipe and it has 10k examples divided into 10 classes:
For the robotic arm:
* Up
* Down
* Right
* Left
* Grab
* Release 

can be used for another application:
* Peace
* Perfect 
* I love you
* Good luck

download the dataset [here](https://drive.google.com/file/d/1wpktVV_S7TxmSbABrLr9mL5WsnYU3d8Z/view?usp=share_link)

## Dataset Sample
![](https://github.com/Muhameddemadd/Hand-Gestures-Recognition/blob/master/Readme_imgs/collage%20(1).jpg)

## Model Architecture
The model uses pre-trained ResNet50 and three more layers to train the data:
* Flatten layer
* Dense layer with 512 neurons with Relu activation function
* Dense layer with 10 neurons: one for each class with sigmoid activation function

![](https://github.com/Muhameddemadd/Hand-Gestures-Recognition/blob/master/Readme_imgs/ResNet%20arch.png)

## Model Summary
![](https://github.com/Muhameddemadd/Hand-Gestures-Recognition/blob/master/Readme_imgs/summary.png)

## The pixel grid approach

By tracking a specific pixel of one landmark of the hand like no.9 which refers to the MIDDLE_FINGER_MCP, we can kow the direction of the hand movement. Assuming that moving right and moving up will increase the values of x and y respectively, For example if the current position of the landmark is (x,y) and the new position is (x+100,y) so the direction of the hand movement is to the right. You can check the whole process in pixel_grid.py 

![](https://github.com/Muhameddemadd/Hand-Gestures-Recognition/blob/master/Readme_imgs/hand_landmarks.png)

But when I applied this to control the robotic arm, it did not work as expected because the processor every time the position changes, it compare it to the old one then send an order to the arm to move, even this takes just some milliseconds, the motors did not move smoothly. So I decided to take the other approach.

