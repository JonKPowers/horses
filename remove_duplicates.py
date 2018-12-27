import os
import pathlib
import re


def main(path=os.getcwd()):
    file_list = get_file_list(path)
    move_duplicates(file_list)

def move_duplicates(file_list):
    possible_duplicates = get_duplicates_list(file_list)
    duplicate_dir = file_list[0].parent.parent / 'duplicate_zips'
    duplicate_dir.mkdir(exist_ok=True)
    for duplicate_file in possible_duplicates:
        original_file = get_original_file(duplicate_file)
        if original_file and original_is_best(original_file, duplicate_file):
            duplicate_file.rename(get_unique_file_name(duplicate_dir, duplicate_file))

def get_original_file(duplicate_file):
    """ Checks whether a non-duplicate style filename exists for a potential duplicate; returns a Path object
        to the original file if found.
    """

    original_file_stem = re.search(r'.+(?= \(\d+\)$)', duplicate_file.stem).group(0)
    original_file_suffix = duplicate_file.suffix
    original_file_name = original_file_stem + original_file_suffix
    original_file_path = pathlib.Path(duplicate_file.parent, original_file_name)
    if original_file_path.exists():
        return original_file_path
    else:
        return None

def get_unique_file_name(path, duplicate_file):
    file_name = duplicate_file.name
    if pathlib.Path(path, file_name).exists():
        i = 0
        while(pathlib.Path(path, file_name).exists()):
            file_name = duplicate_file.stem + str(i) + duplicate_file.suffix
            i += 1
    return pathlib.Path(path, file_name)


def original_is_best(original_file, duplicate_file):
    original_size = os.path.getsize(original_file)
    duplicate_size = os.path.getsize(duplicate_file)
    if original_size == duplicate_size:
        return True
    else:
        return False

def get_file_list(path):
    file_list = [pathlib.Path(path, file) for file in os.listdir(path)]
    file_list = [file for file in file_list if file.is_file()]
    return file_list

def get_duplicates_list(file_list):
    dupe_list = [file for file in file_list if re.search(r'\(\d*\)$', file.stem)]
    return dupe_list

if __name__ == '__main__':
    main()