# Hand-Gestures-Recongnition with ResNet50 used for controlling SCARA Robotic Arm.

Hand gestures detection using Tensorflow, Keras and pre-trained model ResNet50 then applying the final output on real-time application.

 ![](https://github.com/Muhameddemadd/Hand-Gestures-Recognition/tree/master/Readme_imgs)


## Introduction
Snap your fingers and make your coffee maker brew you a fresh cup. Wave a hand near your smart TV and switch on your favorite show. Drag your hand down and drop down the curtains. Grab your hand fist to turn off the lights. How great would it be to get things done just by gesturing? It’s not that unrealistic anymore: hand tracking and gesture recognition technologies are penetrating multiple industries. But do we really need capabilities like these? And what is the true value of real-time hand gesture recognition (HGR)? In this project we will discover how to build a Hand Gestures Recognition model and apply it to a real-time application.

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

## Dataset
### The dataset is manually with mediapipe collected and it has 4k examples divided into 10 classes:
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

## Dataset Sample
![](https://github.com/Muhameddemadd/Hand-Gestures-Detection/blob/master/Readme_imgs/collage%20(1).jpg)

## Model Architecture
The model uses pre-trained ResNet50 and three more layers to train the data:
* Flatten layer
* Dense layer with 512 neurons with Relu activation function
* Dense layer with 6 neurons: one for each class with sigmoid activation function

## Model Summary
![](https://github.com/Muhameddemadd/Hand-Gestures-Detection/blob/master/Readme_imgs/Untitled.jpg)

## The pixel grid approach
Img

By tracking a specific pixel of one landmark of the hand like no.9 which refers to the MIDDLE_FINGER_MCP, we can kow the direction of the hand movement. Assuming that moving right and moving up will increase the values of x and y respectively, For example if the current position of the landmark is (x,y) and the new position is (x+100,y) so the direction of the hand movement is to the right. You can check the whole process in pixel_grid.py 

But when I applied this to control the robotic arm, it did not work as expected because the processor every time the position changes, it comare it to the old one then send an order to the arm to move, even this takes just some milliseconds, the motors did not move smoothly. So I decided to take the other approach.

## Inspiration
AI is slowly seeping to make our lives easier, but it can do more -much more- than controlling a robotic arm -which probably you won’t need in your daily life- here you are some examples you can use Hand Gestures Recognition to escape the ordinary:
* Home automation -check this out
* Automotive check [this](https://www.youtube.com/watch?v=wqvAPskg_k0) out
* Hand gestures to speech and vice versa to communicate with the disabled.
