import cv2 as cv
import os, shutil
import numpy as np
import Util
from PIL import Image
import ctypes, sys


class VideoEncoder:
    def __init__(self, frame_array, output_path, output_file_name):
        self.frame_array = frame_array
        self.current_path = os.path.dirname(os.path.abspath(__file__))

        # Define the codec and create VideoWriter object
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        self.video_writer = cv.VideoWriter(os.path.join(output_path, output_file_name + '.avi'), fourcc, 20.0,
                                           (Util.FRAME_WIDTH, Util.FRAME_HEIGHT))

    def write(self):
        for frame in self.frame_array:
            # code to convert pillow image format to opencv image format
            pil_image = frame.convert('RGB')
            open_cv_image = np.array(pil_image)
            # Convert RGB to BGR
            open_cv_image = open_cv_image[:, :, ::-1].copy()
            self.video_writer.write(open_cv_image)
        self.video_writer.release()

    def write2(self):
        for frame in self.frame_array:
            # code to convert pillow image format to opencv image format
            pil_image = Image.open(os.path.join(self.current_path, 'tmp', frame), 'r')
            pil_image = pil_image.convert('RGB')
            open_cv_image = np.array(pil_image)
            # Convert RGB to BGR
            open_cv_image = open_cv_image[:, :, ::-1].copy()
            self.video_writer.write(open_cv_image)
        self.video_writer.release()
        shutil.rmtree(os.path.join(self.current_path, 'tmp'))
        if Util.is_admin():
            # Code of your program here
            if os.path.exists(os.path.join(self.current_path, 'tmp')):
                pass
            else:
                os.mkdir(os.path.join(self.current_path, 'tmp'))
        else:
            # Re-run the program with admin rights
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            if os.path.exists(os.path.join(self.current_path, 'tmp')):
                pass
            else:
                os.mkdir(os.path.join(self.current_path, 'tmp'))



