from subprocess import PIPE

import os
import configparser
import csv
import re




def commonSort(video_list):
    video_list.sort()
    i = 1
    videoIndexList = []
    for video_name in video_list:
        videoIndexList.append([video_name, i])
        i = i + 1
    return videoIndexList


## 根据名字中第一个连续数字排序
def sortByNum(videoList, index):
    videoIndexList = []
    for videoName in videoList:
        videoindex = getFisrtNum(videoName, index)
        videoIndexList.append([videoName, videoindex])
    videoIndexList = sorted(videoIndexList, key=lambda x: x[0])
    return videoIndexList


def getFisrtNum(videoName, index):
    numlist = re.findall(r'\b\d+\b', videoName)
    if (len(numlist) < 1) or len(numlist) < index:
        return None
    return numlist[index]

config = configparser.ConfigParser()

config.read("conf", encoding="utf-8")

if os.path.exists(config.get("videodir", "dir")):
    if os.path.exists("videolist.csv"):
        os.remove("videolist.csv")
    f = open("videolist.csv", "w")
    writer = csv.writer(f)
    videoList = os.listdir(config.get("videodir", "dir"))
    videoIndexList = sortByNum(videoList, 0)
    for videoName in videoIndexList:
        writer.writerow([videoName[0], videoName[1]])
    print(videoList)
else:
    print("no such video dir")