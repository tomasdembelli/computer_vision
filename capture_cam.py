import os
import sys
from datetime import datetime
try:
    import cv2 as cv
except ModuleNotFoundError:
    print('OpenCV Module not found.')
    sys.exit(1)


class CaptureCam(object):
    """Capture video and save."""

    def __init__(self, cam_id=0, fourcc='XVID', path=os.getcwd(), 
            file_name=None, res=(640, 480), color=True, fps=20):
        """Capture and store video from a camera.
        
        Keyword arguments:
        cam_id: Id number of camera (default 0)
        fourc: Codec (default XVID)
        path: File path (default working directory)
        file_name: File name (Auto assigned if not provided.)
        res: Resolution (default (640, 480))
        color: RGB if True
        fps: Frame per second (default 20)
        """
        self.cam_id = cam_id
        self.cap = cv.VideoCapture(self.cam_id)
        if not self.cap.isOpened():
            self.cap.open()
        self.record_start = False
        # Initiate necessary attributes for saving video.
        if not file_name:
            file_name = ''.join(['Video', '_', datetime.now().strftime('%Y_%m_%d_%H-%M')])
        if not file_name.endswith('.avi'):
            file_name = file_name + '.avi'
        self.file_path = os.path.join(path, file_name)
        self.fourCC = cv.VideoWriter_fourcc(*fourcc)
        self.fps = fps
        self.res = res
        self.color = color
        self.out = False    # Default no recoding.

    def capture(self):
        """Capture video."""
        print('Print "s" to start recording.')
        print(f'Video will be saved to {self.file_path}')
        while(self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret:    # Reading frame is successfull.
                cv.imshow(f' Camera {self.cam_id} View', frame)
                frame_display_duration = 1    # miliseconds
                k = cv.waitKey(frame_display_duration)
                # q for quit, s for saving video.
                if k == ord('q'):    
                    break
                elif (k == ord('s') and not self.record_start):    
                    self.record_start = True
                    self.out = cv.VideoWriter(self.file_path, self.fourCC, 
                                        self.fps, self.res, self.color)
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

    import argparse

    parser = argparse.ArgumentParser(description='Press "s" to \
        start recording and "q" for closing the camera.\
            Without arguments built-in camera will be started and\
                a video file name will be auto generated.')
    parser.add_argument('-c', '--cam', default=0, type=int,
                        help='Camera id - default 0')
    parser.add_argument('-4', '--fourc', default='XVID', type=str,
                        help='Codec - default XVID')
    parser.add_argument('-p', '--path', default=os.getcwd(),type=str,
                        help='Folder to save camera record.')
    parser.add_argument('-f', '--file', default=None, type=str,
                        help='Output file name with the extension.')
    parser.add_argument('-x', '--res', default=(640, 480), type=tuple,
                        help='Resolution - default (640, 480)')
    parser.add_argument('-r', '--rgb', default=True, type=bool,
                        help='Boolean - default True')
    parser.add_argument('-@', '--fps', default=20, type=int,
                        help='fps - default 20')
    args = parser.parse_args()
    
    session = CaptureCam(cam_id=args.cam, fourcc=args.fourc, path=args.path, 
                        file_name=args.file, res=args.res, color=args.rgb, 
                        fps=args.fps)
    session.capture()



        