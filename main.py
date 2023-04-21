import cv2
# Class to perform any of the operations for any given video
class ManipulateVid:
    #Initilialize the object with a path
    def __init__(self, path):
        self.vid = cv2.VideoCapture(path)
    #Resize the frames (with 1/2 the resolution)
    def resize_frames(self):
        while (self.vid.isOpened()):
            success, frame = self.vid.read()
            if (success):
                pass
            else:
                break
    #Reverse the order of the resized frames
    def reverse_order(self):
        pass

def main():
    pass

if __name__ == "__main__":
    main()