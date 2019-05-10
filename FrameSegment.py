from PIL import Image, ImageDraw, ImageFont


class FrameSegment:
    def __init__(self, background_frame):
        # Draw object to put on image
        self.frame_segment = ImageDraw.Draw(background_frame)
