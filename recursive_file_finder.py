import os 

def load_all_txt(root_folder):

    """ Return a list of (file_path, file_content) for every .txt file inside  root folder recursively"""
    all_files=[]

    for folder_path,subfolders,filenames in  os.walk(root_folder):
        for filename in filenames:
            
            if filename.endswith('.txt'):
                full_path =os.path.join(folder_path,filename)
                with open(full_path,'r',encoding='utf-8') as f:
                    content =f.read()
                all_files.append((full_path,content))
                print(f"Found:{full_path}")

    return all_files


files= load_all_txt('my_data')
print(f"\n Total files loaded: {len(files)}")

print(files)
