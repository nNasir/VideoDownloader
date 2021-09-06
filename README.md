# VideoDownloader
Download's YouTube videos and can convert from one format to another

## Downloading Youtube Videos

### Requirements

1)```Python 3```

2)Use following install required python libraries 

```pip install -r requirements.txt```

3)If downloading mp3 files or converting format, download  ```ffmpeg``` 

(https://ffmpeg.org/download.html)

I downloaded ffmpeg windows build by gyan.dev (https://www.gyan.dev/ffmpeg/builds/), 

unzipped it and added the path of ffmpeg/bin to environment variables 

### Script
Add the links of the videos to be downloaded to videoURLs.txt file, one link per line. 
To download mp4 file run following script

```python  downloadvideos.py ```

To download mp3 file run the script as follow

```python downloadvideo.py mp3 ```

Videos will be store in ~/videoCollection folder

## Convert already downloaded videos to another format
Todo





