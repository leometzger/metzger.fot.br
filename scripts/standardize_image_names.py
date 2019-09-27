#!/usr/bin/python3

import os
import getopt
import sys


def rename_files(dir):
    files = os.listdir(dir)

    for idx in range(len(files)):
        src = os.path.join(dir, files[idx])
        dst = os.path.join(dir, str(idx) + ".jpg")
        os.rename(src, dst)


if __name__ == "__main__":
    images_dir = 'public/images'
    subdirs = os.listdir(images_dir)

    for subdir in subdirs:
        directory = os.path.join(images_dir,  subdir)

        if os.path.isdir(directory):
            rename_files(directory)
