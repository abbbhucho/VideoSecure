from moviepy.editor import VideoFileClip, concatenate_videoclips

def videoclips(user_video):
    clip1 = VideoFileClip("./videos/black.mp4")
    clip2 = VideoFileClip(user_video)
    final_clip = concatenate_videoclips([clip2,clip1])
    final_clip.write_videofile(user_video[:-4]+"_hidden.mp4")
