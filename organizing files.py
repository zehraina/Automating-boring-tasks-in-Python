# importing required modules
import os
from shutil import move

# making the directories
root_dir = "C:\\Users\\inaze\\Downloads"
image_dir = "C:\\Users\\inaze\\Downloads\\images"
documents_dir = "C:\\Users\\inaze\\Downloads\\documents"
others_dir = "C:\\Users\\inaze\\Downloads\\others"
software_dir = "C:\\Users\\inaze\\Downloads\\softwares"

# files types of each category
docs = ('.docx', '.doc',  '.txt', '.pdf',
        '.xls', '.ppt', '.xlsx', '.pptx')
images = ('.jpg', '.jpeg', '.png', '.svg',
          '.tif', '.tiff', '.gif',)
softwares = ('.exe', '.dmg', '.pkg')

# appending all the files in the root directory to files[]
files = []
for f in os.listdir(root_dir):
    
    if os.path.isfile(f) and not  f.startswith('.') and not f.__eq__(__file__):
      files.append(f)


# moving files to the respective folders,
# overwriting if needed
for file in files:
    if file.endswith(docs):
        move(file, documents_dir+"/"+file)

    elif file.endswith(images):
        move(file, image_dir+"/"+file)

    elif file.endswith(softwares):
        move(file, software_dir+"/"+file)

    else:
        move(file, others_dir+"/"+file)
