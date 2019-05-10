from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2 as cv

# video/Frame/Image width and height
IMG_WIDTH = 1080
IMG_HEIGHT = 720

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (IMG_WIDTH, IMG_HEIGHT))

# loop for the image generation
for i in range(0, 1500):
    # the top image on the frame
    upperImage = Image.open('./transparent/penguin.png', 'r')

    # the main or the background image
    img = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), color=(73, 109, 137))

    # Draw object to put on image
    d = ImageDraw.Draw(img)

    # font and size for text
    font = ImageFont.truetype("arial.ttf", 26)

    # adding text to the drawing object
    d.text((10 + i, 10), "Hello World", fill=(255, 255, 0), font=font)

    # this line of comment code for saving each frame/image to the local host
    # img.save('p' + str(i) + '.png')

    # pasting upperImage to the background/main image frame
    img.paste(upperImage, (10 + i, 10), upperImage)

    # code to convert pillow image format to opencv image format
    pil_image = img.convert('RGB')
    open_cv_image = np.array(pil_image)
    # Convert RGB to BGR
    open_cv_image = open_cv_image[:, :, ::-1].copy()

    # write the frames to video (.avi)
    out.write(open_cv_image)

out.release()
