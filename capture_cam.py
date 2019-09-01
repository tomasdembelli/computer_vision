import os
import sys
try:
    import cv2 as cv
except ModuleNotFoundError:
    print('OpenCV Module not found.')
    sys.exit(1)
else:
    print('Found OpenCV.')


class CaptureCam(object):
    """Capture video and save."""

    def __init__(self, cam_id=0, fourcc='XVID', path=os.getcwd(), 
            file_name=None, res=(640, 480), color=True, fps=20):
        """Capture and store video from a camera."""
        self.cam_id = cam_id
        self.cap = cv.VideoCapture(self.cam_id)
        if not self.cap.isOpened():
            self.cap.open()

        # If there is file_name, initiate neccessary identifiers.
        if file_name:
            if not file_name.endswith('.avi'):
                file_name = file_name + '.avi'
            self.file_path = os.path.join(path, file_name)
            print(f'Video will be saved to {self.file_path}')
            self.fourCC = cv.VideoWriter_fourcc(*fourcc)
            self.fps = fps
            self.res = res
            self.color = color
            self.record_start = False
        else:
            self.out = False

    def capture(self):
        """Capture video."""
        while(self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret:    # Reading frame is successfull.
                cv.imshow(f' Camera {self.cam_id} View', frame)
                frame_display_duration = 1    # miliseconds
                if cv.waitKey(frame_display_duration) == ord('q'):    # quit
                    break
                elif (cv.waitKey(frame_display_duration) == ord('s') and 
                        self.file_path and not self.record_start):    
                    self.out = cv.VideoWriter(self.file_path, self.fourCC, 
                        self.fps, self.res, self.color)
                    self.record_start = True
                if self.record_start:
                    self.out.write(frame)
            else:
                print('Error at reading frame.')
                sys.exit(1) 

        # Release when finished.
        self.cap.release()
        if self.out:
            self.out.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    session = CaptureCam(file_name='test')
    session.capture()



        