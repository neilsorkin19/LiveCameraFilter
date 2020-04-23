# Live Camera Filter
A camera filter that works in realtime. Script modifiable.

Note: *needs admin privileges*

**Installations**
1. **OBS** (Open Broadcaster Software)
   1. Download here: https://obsproject.com/
   1. This is the base platform from which you can select what windows are shown as input to your virtual camera.
1. **VirtualCam**
   1. Download here: https://github.com/CatxFish/obs-virtual-cam/releases
   1. I recommend installing only 1 virtual camera (default is 4 I think)
   1. I also recommend checking AutoStart once installed.
1. Install **Python**
   1. Download here: https://www.python.org/downloads/
1. Install **PyCharm Community** (Python IDE)
   1. Download here: https://www.jetbrains.com/pycharm/download/
1. Install **pip**
   1. Follow this tutorial: https://phoenixnap.com/kb/install-pip-windows

**Creating the Project**
1. In PyCharm Community (IDE)
   1. File > New Project
   2. Choose the interpreter you installed and name project as you wish
   3. Right click the folder on the left, create new python file with any name
   4. Copy-paste the code from the simple background subtractor .py file
   5. The `cv2` in the first line (`import cv2 as cv`) should be underlined in red.
   6. Right click on it > actions > import opencv-python
   7. It should say something about skeletons at the bottom. Wait to run it until this is done.
   8. Once done right click the tab of the file and run it.
   9. You can change the script to your liking.
   
 **Flow once set up**
 1. Run the .py file
    1. This can be through PyCharm IDE or with the Python interpreter directly
 2. OBS
    1. Launch OBS (with AutoStart preferably)
    2. Use window capture and select "python.exe" for the window
    3. ![Image of OBS Explanation](https://github.com/neilsorkin19/LiveCameraFilter/blob/master/bgSub.PNG)
 3. Once in your program of choice, you should now be able to see "OBS-Camera" as an option. Use that.
 
 Pro tip: When OBS is not running, "OBS-Camera" will still be putting out a video stream, it will just be black.
