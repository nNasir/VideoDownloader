'''
This script is used to download youtbe videos given by user file
The links of the videos to be downloaded should be added to videoURLs.xlxs file, one link per line. 
Videos will be store in ~/videoCollection folder

Prequisites: pip install y

'''
import os
import time
import youtube_dl
import random
import time
from datetime import datetime
import sys

start_time = datetime.now()

# setting paths and reading files
dir_path = os.path.dirname(os.path.realpath(__file__))

dir_urls_csv = dir_path+"/"+"videoURLs.txt"
f=open(dir_urls_csv )
videoURLS = f.read()
videoURLS = [i for i in videoURLS.split("\n") if i!=""]


downloaddir = dir_path+"/videoCollection"
mp3_path=downloaddir+"/mp3"

mp3=False
if len(sys.argv)>1 and sys.argv[1]=="mp3":
    mp3=True

for i in videoURLS:    
    if True:
        print(10)
        ydl = youtube_dl.YoutubeDL({
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=wav]/best', 
            'outtmpl': os.path.join(downloaddir,'%(title)s-%(id)s.%(ext)s')  ,
            'preferedformat': 'mp3',
            'quiet': False
            })
    
        with ydl:
            result = ydl.extract_info(i, download=True)
            # wait for some time
            sleep_seconds= random.randint(10,15)
            time.sleep(sleep_seconds)
            file_name=[f for f in  os.listdir(downloaddir) if i.split("?v=")[1] in f and ".mp4" in f][0]
            print(file_name)
            print('download complete ', i, file_name)
            if mp3:
                print("convert to mp3")
                mp3_file= os.path.join(downloaddir ,file_name.replace(".mp4", ".mp3"))
                mp4_file= os.path.join( downloaddir ,file_name)
                cmd= 'ffmpeg -i "'+ mp4_file + '"'+" "  +'"'+ mp3_file+'"'            
                print(cmd)
                convert=os.system(cmd)
                os.remove(mp4_file)
                  
            
              

