import os
import pathlib

import remove_duplicates
import fix_pp_file_names

def main():
    cwd = os.getcwd()
    remove_duplicates.main(cwd)
    fix_pp_file_names.main(cwd)
    move_zip_files(cwd)

def move_zip_files(path, zip_dir='zip_files', dup_dir='duplicate_zips'):
    file_list = [pathlib.Path(path, file) for file in os.listdir(path)]
    file_list = [file for file in file_list if file.is_file() and file.suffix == '.zip']
    zips_dir = file_list[0].parent.parent / zip_dir
    duplicates_dir = file_list[0].parent.parent / dup_dir
    zips_dir.mkdir(exist_ok=True)
    duplicates_dir.mkdir(exist_ok=True)
    for file in file_list:
        if pathlib.Path(zips_dir, file.name).exists():
            new_file_name = get_unique_file_name(duplicates_dir, file)
        else:
            new_file_name = pathlib.Path(zips_dir, file.name)
        file.rename(new_file_name)

def get_unique_file_name(path, base_file_name):
    file_name = base_file_name.name
    if pathlib.Path(path, file_name).exists():
        i = 0
        while (pathlib.Path(path, file_name).exists()):
            file_name = base_file_name.stem + str(i) + base_file_name.suffix
    return pathlib.Path(path, file_name)

if __name__ == '__main__':
    main()