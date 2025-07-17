# Hand Gesture Image Zoomer (OpenCV)

This project implements a real-time virtual zoom gesture application using OpenCV and the `cvzone` library. It allows users to control the size and position of an image displayed on their webcam feed using specific two-hand gestures.

## Demo

https://github.com/anargh-t/Bank-Loan-Analysis-using-Power-BI-and-SQL/assets/133887240/98a34a37-ba7c-4b79-a1df-99c1a6abeebd

## Features

* **Real-time Hand Tracking:** Utilizes `cvzone` for robust detection of multiple hands.
* **Two-Hand Gesture Recognition:** Specifically detects a two-hand "pinch" or "spread" gesture (index and middle fingers extended on both hands) to trigger zoom.
* **Dynamic Image Scaling:** Adjusts the size of a pre-loaded image based on the distance between the user's index fingertips.
* **Image Positioning:** Centers the zoomed image based on the mid-point of the detected hands.
* **OpenCV Integration:** Leverages OpenCV for camera feed processing and image manipulation.

## How It Works

The system continuously captures video from the default webcam. It then:
1.  Detects if two hands are present in the frame.
2.  Checks for a specific gesture: both hands must have their index and middle fingers extended, simulating a "zoom" or "pinch" action.
3.  Calculates the distance between the tips of the index fingers of both hands.
4.  Compares the current distance to an initial distance (set when the gesture is first recognized) to determine the scaling factor.
5.  Resizes a pre-loaded image (`best-guard-dogs-1650302456.jpeg`) according to this scaling factor.
6.  Overlays the scaled image onto the live webcam feed at the central point between the detected hands.
7.  The zoom amount dynamically changes as the user moves their hands closer or further apart while maintaining the gesture.

## Requirements

Ensure you have Python installed. You can install the necessary libraries using `pip`:

```bash
pip install opencv-python cvzone
