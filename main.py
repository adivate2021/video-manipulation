import cv2
# Class to perform any of the operations for any given video
class ManipulateVid:
    #Initilialize the object with a path
    def __init__(self, path):
        self.vid = cv2.VideoCapture(path)
    #Resize the frames (with 1/2 the resolution) and reverse the video
    def altervid(self):
        resized_list = []
        frameno = 1
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
                cv2.putText(resized_frame, str(frameno), (int(.0463*newwidth),int(.0463*newheight)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 6)
                frameno+=1
                resized_list.append(resized_frame)
            else:
                break
        #Reverse Video
        newvideo = cv2.VideoWriter("newvid.MOV", cv2.VideoWriter_fourcc('m','p','4','v'), 24, (newwidth, newheight))
        for i in range(len(resized_list)):
            newvideo.write(resized_list[len(resized_list)-1-i])
        newvideo.release()
    def space_efficient_altervid(self):
        total_frames = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))
        height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        fps = round(self.vid.get(cv2.CAP_PROP_FPS))
        counter = total_frames - 1
        newvideo = cv2.VideoWriter("newvid.MOV", cv2.VideoWriter_fourcc('m','p','4','v'), fps, (width//2, height//2))
        while (counter >= 0):
            self.vid.set(cv2.CAP_PROP_POS_FRAMES, counter)
            success, frame = self.vid.read()
            if (success):
                #Resize each frame
                height, width, layers = frame.shape
                newheight = height // 2
                newwidth = width // 2
                resized_frame = cv2.resize(frame, (newwidth, newheight))
                cv2.putText(resized_frame, str(counter), (int(.0463*newwidth),int(.0463*newheight)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 6)
                newvideo.write(resized_frame)
                counter-=1
            else:
                break
    #Failed attempt at a faster space efficient method
    '''def faster_space_efficient_altervid(self):
        frameno = 1
        total_frames = round(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))
        height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        fps = round(self.vid.get(cv2.CAP_PROP_FPS))
        newvideo = cv2.VideoWriter("newvid.MOV", cv2.VideoWriter_fourcc('m','p','4','v'), fps, (width//2, height//2))
        while (self.vid.isOpened()):
            success, frame = self.vid.read()
            if (success):
                print(frameno)
                #Resize each frame
                height, width, layers = frame.shape
                newheight = height // 2
                newwidth = width // 2
                resized_frame = cv2.resize(frame, (newwidth, newheight))
                cv2.putText(resized_frame, str(frameno), (int(.0463*newwidth),int(.0463*newheight)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 6)
                frameno+=1
                newvideo.write(resized_frame)
                newvideo.set(cv2.CAP_PROP_POS_FRAMES, 1)
            else:
                break
        newvideo.release()'''

def main():
    a = ManipulateVid("samplevid.MOV")
    a.faster_space_efficient_altervid()

if __name__ == "__main__":
    main()