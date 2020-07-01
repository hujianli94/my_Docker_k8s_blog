#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2020/4/20 8:13
# filename: Delete_staticPhoto.py

"""
此脚本用于删除多于的Static文件。读取所有的md文件，查找图片链接，然后放置到列表中。
未使用图片链接的_static中的文件将被删除

This script is used to delete more than Static files. Read all the md files,
find the picture link, and then put it in the list. Files in _static that are not using image links will be deleted
"""

import os
import sys
import time

CurrentDirectory = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))

# 生成一个使用了图片链接的列表
list_photo = []
Static_Path = CurrentDirectory + "/" + "source/_static"


def trav_walk(pathname):
    '''
    root:当前目录
    dirs：当前目录下的子目录
    files：目录下的所有文件
    '''
    for root, dirs, files in os.walk(pathname):
        for file in files:
            if file.endswith(".png") or file.endswith(".PNG") or file.endswith(".jpg"):
                continue

            fname = os.path.abspath(os.path.join(root, file))
            fname = fname.split("\\")
            if fname[2] == ".git" or fname[2] == ".idea" or fname[2] == "build" or fname[2] == "exts" or fname[
                2] != "source":
                continue
            fname_file = "\\".join(fname)
            if fname_file.endswith(".md"):
                # print(fname_file)
                Read_file(fname_file)


def Read_file(file):
    """ 读文件将使用了图片链接的信息加入到列表中 """
    with open(file, 'r', encoding="utf-8") as fileReader:
        for line in fileReader.readlines():
            line_info = line.strip()
            if line_info.startswith("![]"):
                list_photo.append(line_info.split('/')[-1].strip(")"))


def Delete_picturelink(pathname):
    """
    :param pathname: 存放Static文件的目录
    遍历目录将不在列表中的Static文件删除掉
    :return:
    """
    for root, dirs, files in os.walk(pathname):
        for file in files:
            if file not in list_photo:
                Deltet_fileName = os.path.join(root, file)
                print("delete file : 【{}】".format(Deltet_fileName))
                os.unlink(Deltet_fileName)


if __name__ == '__main__':
    # 遍历文件找到标记信息加入列表
    trav_walk(CurrentDirectory)
    # # 比对列表进行删除操作
    # Delete_picturelink(Static_Path)
