#!/usr/bin/python3

import os, getopt, sys

def rename_files(dir):
  files = os.listdir(dir)

  for idx in range(len(files)):
    src = dir + "/" + files[idx]
    dst = dir + "/" + str(idx) + ".jpg"
    os.rename(src, dst)

if __name__ == "__main__":
  images_dir = 'public/images'
  subdirs = os.listdir(images_dir)

  for subdir in subdirs:
    rename_files(images_dir + "/" + subdir)
