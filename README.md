# Dynamic Object Placement & Video Generation using Stable Diffusion and OpenCV

## Overview

This project dynamically creates composite images by combining an AI-generated background with a user-provided object image. The background is generated using Stable Diffusion based on a user-defined text prompt. Additionally, a zoom-out effect video is generated from the final composite image using OpenCV.

## Features

1. **Text-based Background Generation**: Generates a background image based on a text prompt using the Stable Diffusion model.
2. **Object Image Processing**: Removes the white background of an object image and resizes it dynamically.
3. **Dynamic Object Placement**: Places the object at a random position within the lower half of the background.
4. **Video Creation**: Generates a zoom-out effect video from the final composite image using OpenCV.

## How to Run in Google Colab

### 1. Open Google Colab
Go to [Google Colab](https://colab.research.google.com/) and create a new notebook.

### 2. Install Dependencies
In a code cell, run the following commands to install the necessary libraries:
```python
!pip install --upgrade diffusers transformers -q
```
### 3. Upload Your Object Image
You can upload your object image directly to the Colab environment. Use the following code to upload:

```python
def get_user_input():
    prompt = input("Enter a description for the scene : ")
    return prompt.strip()
```
### 4. Update the Image Path
Set the path for your uploaded object image:

```python
image_path = './example5.jpg'  # Replace with your uploaded image name
```
### 5. Run the Script
Copy and paste the provided Python script (main code) into a code cell, then run it. You will be prompted to enter a description for the background image:

```python
prompt = input("Enter a description for the scene: ")
```
#### 6. Check Output
Once the script completes:

The generated image will be saved as generated_output.png.
The zoom-out effect video will be saved as output_video.mp4.
## Project Structure

├── main.py                     # Main script to generate image and video (to be pasted in Colab)
├── ./example5.jpg              # The object image (to be uploaded)
├── generated_output.png         # The final composite image
├── output_video.mp4             # The generated video
└── README.md                    # This README file
### Approach
## Problem Definition
The objective was to create an automated system that:

Generates an AI-based background using a text prompt.
Processes an object image by removing its white background and resizing it.
Randomly places the object in a visually natural position on the background.
Generates a video with a zoom-out effect using OpenCV.
### Object Processing
The object image is first converted to RGBA format to handle transparency. A function removes any white pixels from the background, making them transparent. The object image is then resized based on the size of the background while maintaining its aspect ratio.

### Background Generation
The user provides a text description (prompt), and the Stable Diffusion model generates a corresponding background image.

### Dynamic Placement
The object is randomly placed within the lower half of the generated background. This ensures that the placement appears natural and prevents the object from being placed out of bounds.

### Video Generation
A zoom-out effect video is created using OpenCV. The effect is achieved by gradually resizing and cropping the center of the image, resulting in a zoom-out animation.

### Example Results
Successful Image Generation
Prompt: "Create a peaceful campsite setting in a lush green forest clearing during late afternoon. The tent is a modern, navy blue and grey dome-shaped camping tent with neon green accents, surrounded by tall pine trees and a serene environment. The sun is setting in the background, casting a soft golden light over the scene. Include a few scattered camping gear items like a backpack, a small campfire with a gentle smoke trail, and a wooden log bench nearby. The sky is clear with soft, glowing clouds, adding a touch of warmth to the atmosphere."


Final Composite Image:
![Successful Image Generation](Avataar-Assignment/generated_output.png)


Zoom-Out Effect Video:
![Zoom-Out Effect Video](/Users/nrawat/Downloads/Avataar2/Avataar-Assignment/output_video.mp4)

Conclusion
This project demonstrates the power of AI-based image generation combined with dynamic object placement and video creation. By automating the process of integrating objects into AI-generated scenes, it offers an exciting way to create visually compelling images and videos.

License
This project is licensed under the MIT License.
