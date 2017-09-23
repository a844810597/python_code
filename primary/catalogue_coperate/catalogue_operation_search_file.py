import os

def search_file(path, dest_file, search_result):
    all_files = os.listdir(path)
    for each_file in all_files:
        if 'System' in each_file or 'Windows' in each_file:
            all_files.remove(each_file)
            
    if all_files == []:
        return
    
    if dest_file in all_files:
            search_result.append(path + dest_file)
    
    for each_file in all_files:
        if os.path.isdir(path + each_file):
            search_file(path + each_file + '\\', dest_file, search_result)
        else:
            continue
    return

path = str(input('请输入要查找路径：'))
file_name = str(input('请输入要查找的文件名：'))
search_result = []
search_file('D:\\python\\', 'zipfile.py', search_result)
for i in range(len(search_result)):
    print(search_result[i])
input('Press the <Enter> to eixt...')
