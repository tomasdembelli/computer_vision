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
