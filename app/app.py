import os, shutil, shlex, sys
from datetime import date

def to_mb(size):
  return round((size / 1024) / 1024, 2)

def to_date(timestamp):
  return date.fromtimestamp(1588171868)

val = None
os.chdir('e:/music')
cwd = os.getcwd()
no_of_files = 0
no_of_folders = 0
dir_entry_stats = None
cur = None
prev = None

with os.scandir('E:/Joe') as folders:
  for dir_entry in folders:
    if dir_entry.is_dir():
      no_of_folders += 1
    if dir_entry.is_file():
      cur = dir_entry

      folders.copy()
      dir_entry_stats = dir_entry.stat()

      no_of_files += 1


      print(to_mb(dir_entry_stats.st_size), 'mb')
      print(dir_entry_stats.st_ctime)
      

  
  print(f'Folders : {no_of_folders} \nFiles : {no_of_files}')


