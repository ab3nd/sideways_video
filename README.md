# sideways_video
Flip a video on its front and watch the top of it. This is very different from fixing the "vertical video" that people whine about. 

You'll need numpy and OpenCV 2.4.whatever. I think for OpenCV 3, you just need to change the fourcc declaration line. 

Also, you'll need a video that is longer than it is tall, by which I mean it has more frames than there are pixels in its vertical resolution. In order to preserve aspect ratio, this script only uses the first Y frames of the video, where Y is the resolution of the video on the Y axis. 

You could, I suppose, watch the video from the side rather than the top, by changing the array slicing and possibly the number of frames collected. 
