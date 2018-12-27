import os
import pathlib
import zipfile
import re
import tempfile
import shutil

def main():
    cwd = os.getcwd()
    extracted_dir = pathlib.Path(cwd).parent / 'extracted_files'
    extracted_dir.mkdir(exist_ok=True)
    processed_dir = pathlib.Path(cwd).parent / 'processed_zip_files'
    processed_dir.mkdir(exist_ok=True)
    file_list = get_file_list(cwd)
    file_list = [file for file in file_list if file.suffix.lower() == '.zip']   # Make sure only using zip files

    for file in file_list:
        if is_pp_file(file):
            with tempfile.TemporaryDirectory() as temp_dir:
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    zipfile_list = zip_ref.infolist()
                    year = zipfile_list[0].date_time[0]
                    try:
                        assert(len(zipfile_list) == 1)
                    except AssertionError:
                        print('Unexpectedly found more or less than 1 file in PP zip file')
                        continue
                    zip_ref.extractall(path=temp_dir)
                    unzipped_files = [pathlib.Path(temp_dir, file) for file in os.listdir(temp_dir)]
                    for unzipped_file in unzipped_files:
                        new_file = pathlib.Path(temp_dir, unzipped_file.stem + str(year) + unzipped_file.suffix)
                        unzipped_file.rename(new_file)
                        move_to_dir(new_file, extracted_dir)
        else:
            with tempfile.TemporaryDirectory() as temp_dir:
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    zip_ref.extractall(path=temp_dir)
                    unzipped_files = [pathlib.Path(temp_dir, file) for file in os.listdir(temp_dir)]
                    for unzipped_file in unzipped_files:
                        move_to_dir(unzipped_file, extracted_dir)
        move_to_dir(file, processed_dir)

def move_to_dir(file, dir):
    new_file_name = pathlib.Path(dir, file.name)
    if new_file_name.exists():
        new_file_name = get_unique_file_name(file, dir)
    try:
        file.rename(new_file_name)
    except OSError:
        shutil.copy(str(file), str(new_file_name))

def get_unique_file_name(file, path):
    file_name = file.name
    if pathlib.Path(path, file_name).exists():
        i = 0
        while (pathlib.Path(path, file_name).exists()):
            file_name = file.name + '_' + str(i)
            i += 1
    return pathlib.Path(path, file_name)

def is_pp_file(file):
    """ Checks whether the zip file contains a PP data file, which ends with the .DRF suffix"""
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_info = zip_ref.infolist()
        test_file = zip_info[0]
        name = test_file.filename.lower()
        if name.endswith('drf'):
            return True
        else:
            return False


def get_file_list(path):
    file_list = [pathlib.Path(path, file) for file in os.listdir(path)]
    file_list = [file for file in file_list if file.is_file()]
    return file_list

if __name__ == '__main__':
    main()