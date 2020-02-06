Convert any video clip into bar form or save all its frames.

### Update v003
* Barcode mode change to optional(-b).
* Module check script added.
* Tweaks to make the script faster.

## Installation
```
pip3 install -r requirements.txt
```

## Usage
```
python3 mvbar [mp4_file]
```
```
Optional --
-b, --bar       Create barcode of the images
-s, --save      Save all the frames of the video clip
-v, --verbose   Enable Verbose mode
```

### Next Update
* Multiprocessing enabled to increase the speed of the script.

### Previous Updates

#### Update v002
* Added verbose mode(progress bar).
* Fixed bug: Last frame imwrite error.

##### Update v001
* Added option to save every frame of a video.
* All the data generated by script will be saved in a separate folder.
* Corrected error handling in naming the folders.
