from PIL import ImageFont


class TextComponent:
    def __init__(self, parent_frame, text, x, y):
        # font and size for text
        font = ImageFont.truetype("arial.ttf", 26)

        # adding text to the drawing object
        parent_frame.text((x, y), text, fill=(255, 255, 0), font=font)
