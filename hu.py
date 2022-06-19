# importing required modules
if __name__ == "__main__":
  

  import os
  from shutil import move

# making the directories
  user = (os.environ.get('USERNAME'))
  root_dir = '/Users/{}/Downloads/'.format(user)
  image_dir = '/Users/{}/Downloads/images/'.format(user)
  documents_dir = '/Users/{}/Downloads/documents/'.format(user)
  others_dir = '/Users/{}/Downloads/others/'.format(user)
  software_dir = '/Users/{}/Downloads/softwares/'.format(user)

# files types of each category
  doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
  img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
  software_types = ('.exe', '.pkg', '.dmg')

#appending all the files in the root directory to files[]
  files = []
  for f in os.listdir(root_dir):
    
    if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__):
      files.append(f)
        
#moving the files to the respective folders, overwriting if needed
  for file in files:
    
    if file.endswith(doc_types):
      move(file, '{}/{}'.format(documents_dir, file))
      print('file {} moved to {}'.format(file, documents_dir))
    elif file.endswith(img_types):
      move(file, '{}/{}'.format(image_dir, file))
      print('file {} moved to {}'.format(file, image_dir))
    elif file.endswith(software_types):
      move(file, '{}/{}'.format(software_dir, file))
      print('file {} moved to {}'.format(file, others_dir))
    else:
      move(file, '{}/{}'.format(others_dir, file))
      print('file {} moved to {}'.format(file, others_dir))
            
