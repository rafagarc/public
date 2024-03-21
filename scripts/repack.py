import os
import shutil
from time import sleep

print(f'Hi. This will rename all files in tollowing folder and place them in a nested folder: \n\n{os.getcwd()}\n')

print('Proceed with caution.')

sure = input('Are you sure? (y/n)> ')

my_prefix = input('Name your prefix and folder: ')

def rename_files(folder_path, prefix):
    counter = 0
    for filename in os.listdir(folder_path):
        # make sure file is not folder
        if os.path.isfile(os.path.join(os.getcwd(), filename)):
        
            # Get filename and extension separately
            file_name, extension = os.path.splitext(filename)
            
            # Create new filename with prefix, counter, and extension
            new_filename = f"{prefix}_{str(counter).zfill(4)}{extension}"
            
            # Construct full paths for old and new files
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            
            # Rename the files (except script)
            if '.py' not in old_path:
                os.rename(old_path, new_path)
                counter += 1
            else:
                pass
    print('Files renamed.')

def create_folder_and_move_files(my_foldername):
    # Get the current working directory
    current_directory = os.getcwd()

    # Create a nested folder inside the current working directory
    nested_folder_name = my_foldername
    nested_folder_path = os.path.join(current_directory, nested_folder_name)
    os.makedirs(nested_folder_path, exist_ok=True)

    # Get a list of all files in the current working directory
    files = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]

    # Move each file to the nested folder
    for file_name in files:
        # make sure you don't move the scripts
        if '.py' not in file_name:
            source_path = os.path.join(current_directory, file_name)
            destination_path = os.path.join(nested_folder_path, file_name)
            shutil.move(source_path, destination_path)
            print(f"Moved '{file_name}' to '{nested_folder_name}' folder.")
        else:
            pass

if sure.lower() == 'y':
    rename_files(os.getcwd(), my_prefix)
    create_folder_and_move_files(my_prefix)
    print('Operation complete.')
    sleep(5)
else:
    print('Aborting operation')
    sleep(5)