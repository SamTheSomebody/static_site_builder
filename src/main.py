import os
import shutil

def main():
    dest_path = os.path.realpath("public")
    print(f"Destination path is: {dest_path}")
    src_path = os.path.realpath("static")
    print(f"Source path is: {src_path}")

    if os.path.exists(dest_path):
        print(f"Removing directory: {dest_path}")
        shutil.rmtree(dest_path, ignore_errors = False)
    os.mkdir(dest_path)

    copy_file(src_path)
    #Recursive Function
    #Move all files and folders from static to public
    #Delete all files in public

def copy_file(path):
    print(f"Looking through: {path}")
    sub_paths = os.listdir(path)
    for sub_path in sub_paths:
        print(sub_path)
        full_path = os.path.join(path, sub_path)
        dest_path = full_path.replace("/static/", "/public/")
        print(f"Copying: {full_path} to: {dest_path}")
        if os.path.isfile(full_path):
            shutil.copy(full_path, dest_path)
        else:
            os.mkdir(dest_path)
            copy_file(full_path)

main()
