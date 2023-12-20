# HeritageShield
# SIH 2023

## Vandalism Detection System (YOLOv8 Ultralytics)

### Overview

The Vandalism Detection System is a pioneering solution in heritage site preservation, marking the first time in the world such advanced technology has been employed for vandalism identification. It utilizes the YOLOv8 Ultralytics model, integrated with PyTorch and semantic segmentation techniques. This system is uniquely designed to accurately distinguish between actual vandalism and legitimate decorative elements of heritage sites, using a custom-built vandalism dataset of 6,000 images enhanced with Albumentations and augmentation techniques.

### Key Features

- World's First Advanced Vandalism Detection
  
First-of-its-kind implementation using YOLOv8 Ultralytics model.
Custom-made dataset of 6,000 images specifically for vandalism detection.
  
- Enhanced Accuracy with Semantic Segmentation
  
Employs semantic segmentation to discern vandalism from legitimate designs.
Significantly reduces false positives.

- Integration with Surveillance Systems
  
Seamlessly integrates with existing CCTV and surveillance infrastructure.

- Real-time Alerts
  
Instant notifications to site personnel upon detection of vandalism.

### System Requirements

Python 3.6 or later.
PyTorch 1.8 or later.
Ultralytics YOLOv8 package.
Compatible hardware for running deep learning models (GPU recommended).

## Litter Detection Model
The YOLOv8 Ultralytics Litter Detection Model, developed using PyTorch, represents a cutting-edge approach to environmental cleanliness.
It utilizes the latest YOLO (You Only Look Once) version 8 for real-time object detection, specifically trained to identify various types of litter with high accuracy.
The model's efficiency lies in its speed and precision, making it ideal for monitoring public spaces, parks, and heritage sites.

## Reverse Lost and found System
### Overview

The Reverse Lost and Found System is an innovative solution employing BlazeFace, MediaPipe, Ultralytics, and OpenCV for effective backtracking. This system is designed to identify and return lost items to their owners by analyzing surveillance footage in public spaces, parks, and heritage sites.

### Key Features

- Advanced Object and Facial Recognition
  
Utilizes BlazeFace for facial recognition and MediaPipe for advanced object tracking.
Employs Ultralytics for object detection to identify lost items.

- Efficient Backtracking Algorithm
  
Implements OpenCV for real-time video processing and backtracking lost items to their owners.
Traces the movement of individuals and items in reverse to locate the point of loss.

- Integration with Surveillance Systems
  
Seamlessly integrates with existing camera and surveillance infrastructure.

- User-Friendly Interface
Provides a simple and intuitive interface for system operators to manage lost and found items.

### System Requirements

- Python 3.6 or later.
- BlazeFace, MediaPipe, Ultralytics, and OpenCV libraries.
- Compatible hardware for processing video feeds (GPU recommended).

## Heritage Site Personnel Portal
![PHOTO-2023-12-19-20-29-44](https://github.com/gopal-ag/HeritageShield/assets/109476637/83f557f7-819f-4ca9-aeb9-c8a5e5ff6120)
![PHOTO-2023-12-19-20-30-13](https://github.com/gopal-ag/HeritageShield/assets/109476637/be001f48-2a37-453e-a0df-1bdb18635564)

### Overview

The Heritage Site Personnel Portal is designed to assist the staff of heritage sites in monitoring and managing various aspects of the site. This includes tracking vandalism, managing the number of visitors, handling littering issues, overseeing lost and found requests, and monitoring the status of electronic fines (e-Chalaans).

### Features
- Vandalism Monitoring
  
Displays photos of individuals caught vandalizing the monument.
Shows the specific camera that captured the vandalism.
Includes a button to issue a fine, which is sent via WhatsApp.

- Visitor Count
  
Real-time tracking of the number of people present in the monument at any given time.

- Littering Culprits
  
Displays photos of individuals caught littering.
Indicates the specific camera that captured the littering incident.

- Lost and Found Management
  
Tracks lost and found requests.
Utilizes backtracking to locate lost or found objects.
Backtracking in the context of identifying the owner of lost objects at a heritage site involves analyzing security camera footage to trace the movements and actions of individuals, particularly those who have lost or found items. This process aims to establish a connection between the object and its rightful owner

- E-Chalaan Status
Provides information on previously sent e-Chalaans, including the date sent and the deadline for payment.

## Monument Ticket Booking System

![PHOTO-2023-12-19-12-47-48](https://github.com/gopal-ag/HeritageShield/assets/109476637/c6c588c4-05c7-47c9-b9f1-3ead97bf7fab)

### Overview

The Monument Ticket Booking System is an intuitive online platform that allows users to book tickets for various monuments based on their current GPS location. The system displays nearby monuments, provides ticket prices, and facilitates easy booking and payment.

### Features

- GPS-Based Monument Identification
  
Automatically identifies monuments near the user's location.
Displays monuments in the form of cards, including details like ticket prices and location.

- Easy Ticket Booking
Offers a direct booking button on each monument card.
Provides three methods for filling out the booking form:
1. Using a webcam.
2. Manual entry.
3. Uploading files from the user's system.
   
- Secure Payment Processing
  
Redirects to a payment page after form submission.
Supports various payment methods for user convenience.

- Ticket Generation and Download
  
Generates a ticket upon successful payment.
Offers an option to download the ticket for easy access and future reference.
