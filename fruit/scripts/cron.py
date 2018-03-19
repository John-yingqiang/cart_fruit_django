#! /usr/bin/python
import os, stat

def get_all_files(path):
    for root, diten, files in os.walk(path):
        return files

def modify_mod(root, file_s):
    mod_old = oct(os.stat(root + '/' + file_s).st_mode)[-3:]
    if mod_old != 644:
        os.chmod(root + '/' + file_s, stat.S_IRWXU|stat.S_IRGRP|stat.S_IROTH)

local_file_path = '/home/john/sites/www.thaifruit1975.com/Thai/fruit/static/media'

files=get_all_files(local_file_path)
for file_s in files:
    modify_mod(local_file_path, file_s)



