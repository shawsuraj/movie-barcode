# Videos Something!

Convert any video clip into bar form or save all its frames.

<div align="center">

  [![Build Status](https://travis-ci.com/shawsuraj/movie-barcode.svg?branch=master)](https://travis-ci.com/shawsuraj/movie-barcode)
  <a href="https://github.com/shawsuraj/movie-barcode/releases">
    <img title="GitHub version" src="https://img.shields.io/badge/Version-v1.5-brightgreen" >
  </a>
  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
  <br>
  [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

</div>

## Getting Started

A python based script to do something with videos.

### Prerequisites

Basic requirement to run the script : python3, pip3 and git.

If these are not installed or if you don't know, run the following commands

**Linux:**
```
$ sudo apt-get install python3 pip3 git
```

**Unix:**
```
$ sudo brew install python3 git
```

**Windows:**
<a href ="https://www.python.org/downloads/windows/"> Donwload python</a>

### Installing

A step by step series of examples that tell you how to get a development env running

Clone this repo and then install the modules.
```
$ git clone https://github.com/shawsuraj/movie-barcode
$ cd movie-barcode
$ pip3 install -r requirements.txt
```

End with an example of getting some data out of the system or using it for a little demo

## Usage
```
$ python3 mvbar.py -f [mp4_file]
```
OR
```
$ python3 mvbar.py -u [URL]
```
```
Optional --
-f abc.mp4, --file abc.mp4 Location of the video file
-u https://youtu.be/xyz, --url https://youtu.be/xyz  Url of the video
-b, --bar             Create barcode of the video
-s, --save            Save the frames of a video
-v, --verbose         Show progress
-t, --time            Capture from a specific time. format => hh:mm:ss-hh:mm:ss
```

## Example

### Capture frames Only of a video file
```
python3 mvbar.py -s -f abc.mp4
```

### Capture frames and also create barcode from youtube
```
python3 mvbar.py -bs -u http://youtube.com/abc123
```

### Show progress and capture frames and create barcode from a local video file
```
python3 mvbar.py -bsv -t 00:05:00-00:07:30 -f abc.mp4
```

### Capture frames only of a file from a start time to end
```
python3 mvbar.oy -bv -t 00:06:30-00:00:00 -f abc.mp3
```

## Author

**Suraj Shaw**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

---

## Tasks

- [ ] Add multiprocessing
- [ ] Add option to condense the bar ,
- [x] Add Youtube videos support (pafy)
- [x] Add option to define time
- [ ] GUI version

---  
