from subprocess import PIPE

import os
import configparser
import csv

config = configparser.ConfigParser()

config.read("conf", encoding="utf-8")


if os.path.exists(config.get("videodir", "dir")):
    if os.path.exists("videolist.csv"):
        os.remove("videolist.csv")
    f = open("videolist.csv", "w")
    writer = csv.writer(f)
    video_list = os.listdir(config.get("videodir", "dir"))
    video_list.sort()
    i=1
    for video_name in video_list:
        writer.writerow([video_name, i])
        i = i+1
    print(video_list)
else:
    print("no such video dir")