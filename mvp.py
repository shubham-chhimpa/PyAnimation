from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2 as cv

IMG_WIDTH = 1080
IMG_HEIGHT = 720

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (IMG_WIDTH, IMG_HEIGHT))

for i in range(0, 100):
    upperImage = Image.open('./transparent/penguin.png', 'r')
    img = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), color=(73, 109, 137))
    d = ImageDraw.Draw(img)

    font = ImageFont.truetype("arial.ttf", 26)

    d.text((10 + i, 10), "Hello World", fill=(255, 255, 0), font=font)
    # img.save('p' + str(i) + '.png')

    upperImage_w, upperImage_h = upperImage.size

    img_w, img_h = img.size

    img.paste(upperImage, (10 + i, 10), upperImage)

    pil_image = img.convert('RGB')
    open_cv_image = np.array(pil_image)
    # Convert RGB to BGR
    open_cv_image = open_cv_image[:, :, ::-1].copy()

    # frame = cv.imread('p' + str(i) + '.png')

    # write the flipped frame
    out.write(open_cv_image)

out.release()
