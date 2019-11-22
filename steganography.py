import sys, os
import image_merge as image
import hide_text as text
import merge as merge
import make as make

def main():
    if(len(sys.argv) > 2):
        user_video = sys.argv[1] 
        cover_path = "./images/images.jpg"
        steg(cover_path, sys.argv[2])
        make.convert_frames_to_video('./images/', './videos/black.mp4', 10)
        merge.videoclips(user_video)
    else:
        hidden_video = sys.argv[1]

        cover_path = "./images/images_hidden.bmp"
        desteg(cover_path)


def steg(cover_path, hidden_path):
    '''
    Function to hide data (either an image or text) within another image
    INPUT: string, path to the cover image; string, path to the hidden data
    OUTPUT: a new image with the hidden data encoded in the least significant
    bits
    '''
    if hidden_path[-4:] == '.txt':
        text.encrypt(cover_path, hidden_path)
    else:
        image.merge(cover_path, hidden_path)


class FException(Exception):
    pass
   
    
def desteg(path):
    '''
    Function to decode hidden data in an image
    INPUT: string, path to the coded image
    OUTPUT: If hidden data is an image, the hidden image is saved. If hidden
            data is text, the text is saved.
    '''
    try:
        if os.path.exists(path):
            text.decrypt(path)
        else:
            raise FException()

    except FException:
        path = './images/merged.png'
        image.unmerge(path)


if __name__ == "__main__":
    main()
