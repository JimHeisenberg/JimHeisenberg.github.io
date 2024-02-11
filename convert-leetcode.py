import sys
import os
import time


# convert all files in _drafts into the format of files in _posts
# then delete all files in _drafts and create new files in _posts


# config tag appearing in headers
tags = ["leetcode75"]


# path config
path = os.getcwd()
draftsPath = path + "\\_drafts\\"
postsPath = path + "\\_posts\\"
fileNames = os.listdir(draftsPath)


for fileName in fileNames:
    fileInfo = os.stat(draftsPath + fileName)
    modifiedTime = time.strftime("%Y-%m-%d %H:%M:%S",
                                 time.localtime(fileInfo.st_mtime))
    fileNamePrefix = time.strftime("%Y-%m-%d-",
                                   time.localtime(fileInfo.st_mtime))
    headers = []
    headers.append("---\n")
    headers.append("layout: post\n")
    headers.append(f"date: {modifiedTime} +0800\n")
    tags_str = ""
    for tag in tags:
        tags_str += ' ' + tag
    headers.append(f"tags:{tags_str}\n")
    headers.append("---\n")
    headers.append("\n")
    # delete files in drafts and create corresponding files in posts
    with open(draftsPath + fileName, mode="r+", encoding="UTF-8") as f:
        content = f.readlines()
    with open(postsPath + fileNamePrefix + "leetcode75" + fileName, mode="x+", encoding="UTF-8") as f:
        f.writelines(headers)
        f.writelines(content)
    os.remove(draftsPath + fileName)
