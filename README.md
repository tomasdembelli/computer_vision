# computer_vision
Image and video processing with Python.

#### Examples

A connected camera can be turned on and a footage can be recorded.

Using the `CaptureCam()` object without argument will start built-in webcam and auto assign a name for the video.
```Python
>>> from capture_cam import CaptureCam
>>> session = CaptureCam()
>>> session.capture()
Print "s" to start recording.
Video will be saved to [working/directory/]Video_2019_09_03_22-49.avi
```

`capture_cap.py` can be started from command line.
```Bash
python3 capture_cam.py -h
usage: capture_cam.py [-h] [-c CAM] [-4 FOURC] [-p PATH] [-f FILE] [-x RES]
                      [-r RGB] [-@ FPS] [-a FACE_DETECT] [-e EYE_DETECT]

Press "s" to start recording and "q" for closing the camera. Without arguments
built-in camera will be started and a video file name will be auto generated.

optional arguments:
  -h, --help            show this help message and exit
  -c CAM, --cam CAM     Camera id - default 0
  -4 FOURC, --fourc FOURC
                        Codec - default XVID
  -p PATH, --path PATH  Folder to save camera record.
  -f FILE, --file FILE  Output file name with the extension.
  -x RES, --res RES     Resolution - default (640, 480)
  -r RGB, --rgb RGB     Boolean - default True
  -@ FPS, --fps FPS     fps - default 20
  -a FACE_DETECT, --face_detect FACE_DETECT
                        Face detection - default False.
  -e EYE_DETECT, --eye_detect EYE_DETECT
                        Eye detection - default False.

```
