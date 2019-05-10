import VideoSegment as vs

my_video_segment1 = vs.VideoSegment((73, 109, 137), 360)
my_video_segment1.add_text_component("this is the text",list(range(10,20)),150,130)

# my_video_segment1.add_image_component('./transparent/penguin.png',list(range(10,20)),100,100)


# my_video_segment2 = vs.VideoSegment((255, 109, 137),10)
# my_video_segment1.add(my_video_segment2)
# print(len(my_video_segment1.frame_array))
# my_video_segment1.save('output', 'test2')
my_video_segment1.save2('output', 'test2')
