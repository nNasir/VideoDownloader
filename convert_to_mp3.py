'''
This script is used to convert MP4 videos to mp3

'''
#!/usr/bin/env python3

import os




# setting paths and reading files
dir_path=os.path.dirname(os.path.realpath(__file__))

mp4_path=dir_path+"/videoCollection"
mp3_path=mp4_path+"/mp3"

mp4files= os.listdir(mp4_path)
mp4files=[i for i  in  mp4files if i.split(".")[-1]=="mp4"]


for file in mp4files:
    outfile= os.path.join(mp3_path, file).replace(".mp4", ".mp3")
    if  not os.path.exists(outfile):
        cmd= 'ffmpeg -i "'+ os.path.join(mp4_path, file) + '"'+" "  +'"'+ outfile+'"'
        print(cmd)
        os.system(cmd)


