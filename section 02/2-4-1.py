import os
import subprocess
import pytube

yt = pytube.YouTube("https://youtu.be/CTRO5NXmAp8")
vids = yt.streams.all()


for i in range(len(vids)):
    print(i, ',',vids[i])

down_dir="D:/gms/Atom"

vids[0].download(down_dir)
