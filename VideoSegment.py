from PIL import Image, ImageDraw, ImageFont
import FrameSegment as fs
import TextComponent as tc
import ImageComponent as ic
import VideoEncoder as ve
import Util
import os
import ctypes, sys



class VideoSegment:

    def __init__(self, background_color, duration):
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.duration = duration
        self.background_color = background_color
        self.frame_array = []
        self.frame_array_size = 0

        # # the main or the background image
        # self.background_frame = Image.new('RGB', (Util.FRAME_WIDTH, Util.FRAME_HEIGHT), color=self.background_color)
        #
        # # loop for the image generation
        # for i in range(0, duration * 20):
        #     self.frame_array.append(self.background_frame.copy())
        #     # self.frame_array_size = self.frame_array_size + background_frame.
        #     # print(self.frame_array_size)
        #     # print(background_frame)
        #     print("no: " + str(i))
        #     self.frame_array_size = self.frame_array_size + sys.getsizeof(self.background_frame)
        #     print(self.frame_array_size / 1024)

      ##################################################

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

        self.background_frame = Image.new('RGB', (Util.FRAME_WIDTH, Util.FRAME_HEIGHT), color=self.background_color)
        for i in range(0, duration * 20):
            self.background_frame.save(os.path.join(self.current_path,'tmp','frame' + str(i) + '.png'))
            self.frame_array.append('frame' + str(i) + '.png')




    def save(self, output_path, output_file_name):
        print(len(self.frame_array))
        video_encoder = ve.VideoEncoder(self.frame_array, output_path, output_file_name)
        video_encoder.write()

    def save2(self ,output_path, output_file_name):
        print(self.frame_array)
        video_encoder = ve.VideoEncoder(self.frame_array, output_path, output_file_name)
        video_encoder.write2()

    def set_duration(self, duration):
        self.duration = duration

    def add(self, video_segment_object):
        self.frame_array = self.frame_array + video_segment_object.frame_array

    def add_text_component(self,text, at, x, y):
        for i in at:
            frame = Image.open(os.path.join(self.current_path, 'tmp','frame' + str(i) + '.png'), 'r')
            frame_segment = fs.FrameSegment(frame).frame_segment
            text_component = tc.TextComponent(frame_segment, text, x, y)
            frame.save(os.path.join(self.current_path, 'tmp', 'frame' + str(i) + '.png'))

    def add_image_component(self,image_path, at,x, y):
        for i in at:
            image_component = ic.ImageComponent(image_path,self.frame_array[i], x, y)


