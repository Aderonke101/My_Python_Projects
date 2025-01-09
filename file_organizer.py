#Set Up the ProjectImport necessary modules:os and shutil to interact with the file system.os.path to manipulate paths.import os
import shutil
from pathlib import Path

#File Type DetectionDefine common file types that your script will categorize:
FILE_TYPES = {
'Images':['.jpg', '.jpeg', '.png', '.gif'],
'Documents': ['.pdf', '.docx', '.txt'],
'Videos': ['.mp4', '.mov', '.avi'],
    # Add more as needed
}
#Directory CreationCreate subdirectories within the main directory for different file types:
import os
def create_directories(base_directory):
    for category in:
FILE_TYPES.keys():
folder_path =
os.path.join('base_directory,category')
if not
os.path.exists(folder_path)
os.makedirs(folder_path)

#File Movement Move files to their respective directories based on their types:
def move_file(file, base_directory):
    file_extension = Path(file).suffix.lower()
    for category, extensions in FILE_TYPES.items():
        if file_extension in extensions:
            shutil.move(file, os.path.join(base_directory, category, os.path.basename(file)))
            return category
    return None
#User Interaction Allow users to specify the directory to be organized:
def organize_directory():
    base_directory = input("Enter the directory to organize: ")
    create_directories(base_directory)

    # Loop through the files in the directory
    for item in os.listdir(base_directory):
        item_path = os.path.join(base_directory, item)
        
        # Only process files (skip directories)
        if os.path.isfile(item_path):
            category = move_file(item_path, base_directory)
            if category:
                print(f"Moved {item} to {category}")
            else:
                print(f"File type for {item} not recognized.")
    #Run the ScriptSimply call the function to run the script:
if __name__ == "__main__":
    organize_directory()

    #Provide FeedbackThe script already prints feedback on the files moved. 

    def organize_directory():
    base_directory = input("Enter the directory to organize: ")
    create_directories(base_directory)
    
    files_moved = 0
    unrecognized_files = 0
import os
for item in
os.listeddir(base_directory):
item_path = 
os.path.join(base_directory, item)
if
os.path.isfile(item_path)
category = 
move_file(item_path, base_directory)
if category:
      print(f'Moved {item} to {category}')
      files_moved += 1
else:
      print(f'file type for {item} not recognized.')
      unrecognized_files +=1
    
print(f"\nSummary: {files_moved} files moved, {unrecognized_files} files unrecognized.")
