#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 07:30:11 2018

@author: jkpowers
"""

import os
import pathlib
import re
import zipfile



def main(path=os.getcwd()):
    file_list = get_pp_file_list(get_file_list(path))
    for file in file_list:
        # Skip file if it already has MMDDYYYY in the filename
        if has_full_pp_date(file):
            continue

        # Add YYYY to the file name
        year = get_year(file)
        new_file_name = file.stem[:-1] + year + 'k' + file.suffix
        if pathlib.Path(file.parent, new_file_name).exists():
            i = 0
            while(pathlib.Path(file.parent, new_file_name).exists()):
                new_file_name = file.stem + str(i) + file.suffix
                i += 1
        new_file_path = pathlib.Path(file.parent, new_file_name)
        file.rename(new_file_path)

def has_full_pp_date(file):
    """ Checks whether the filename already has a MMDDYYYY format in filename. Returns True if it
        does; otherwise False
    """
    file_stem = file.stem
    if re.search(r'[a-zA-z]\d{8,9}k$', file_stem):
        return True
    else:
        return False

def get_year(file):
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_info = zip_ref.infolist()
        date_info = zip_info[0].date_time
        year = date_info[0]
        return str(year)

def get_file_list(path):
    file_list = [pathlib.Path(path, file) for file in os.listdir(path)]
    file_list = [file for file in file_list if file.is_file()]
    return file_list

def get_pp_file_list(file_list):
    pp_file_list = [file for file in file_list if file.stem.endswith('k')]
    return pp_file_list

if __name__ == '__main__':
    main()