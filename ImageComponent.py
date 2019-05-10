from PIL import Image


class ImageComponent:
    def __init__(self,image_path,parent_image, x, y):
        # the top image on the frame
        image = Image.open(image_path, 'r')
        # pasting upperImage to the background/main image frame
        parent_image.paste(image, (x, y), image)
