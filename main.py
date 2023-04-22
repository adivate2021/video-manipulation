import cv2
# Class to perform any of the operations for any given video
class ManipulateVid:
    #Initilialize the object with a path
    def __init__(self, path):
        self.vid = cv2.VideoCapture(path)
    #Resize the frames (with 1/2 the resolution) and reverse the video
    def altervid(self):
        resized_list = []
        while (self.vid.isOpened()):
            success, frame = self.vid.read()
            '''cv2.imshow('Frame',frame)
            if cv2.waitKey(5000) & 0xFF == ord('q'):
                 break'''
            if (success):
                #Resize each frame
                height, width, layers = frame.shape
                newheight = height // 2
                newwidth = width // 2
                resized_frame = cv2.resize(frame, (newwidth, newheight))
                resized_list.append(resized_frame)
            else:
                break
        #Reverse Video
        newvideo = cv2.VideoWriter("newvid.MOV", cv2.VideoWriter_fourcc('m','p','4','v'), 24, (newwidth, newheight))
        for i in range(len(resized_list)):
            newvideo.write(resized_list[len(resized_list)-1-i])
        newvideo.release()

def main():
    a = ManipulateVid("samplevid.MOV")
    a.altervid()

if __name__ == "__main__":
    main()