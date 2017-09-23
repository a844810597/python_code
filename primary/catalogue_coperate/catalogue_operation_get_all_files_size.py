import os
  # 所有涉及路径的参数，都要求是绝对路径

def get_all_files_size(path = os.curdir):
    all_files = os.listdir(path)
    size_dict = dict()
    
    for each_file in all_files:
        if os.path.isfile(path + each_file):
            size_dict.setdefault(each_file, os.path.getsize(path + each_file))
    return size_dict

print(get_all_files_size('E:\\'))
