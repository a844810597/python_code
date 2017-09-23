import os


def find_all_specific_type_files(dest_files, path=os.curdir, *file_type):  # 收集参数，将所有剩下的参数打包为元组
    all_files = os.listdir(path)
    for each_file in all_files:
        
        if 'System' in each_file or 'Windows' in each_file:  # 跳过以'System'和'Windows'开头的无访问权限的文件
            all_files.remove(each_file)
        elif os.path.isdir(path + each_file + os.sep):  # 如果改文件是文件夹，则递归访问寻找
            find_all_specific_type_files(dest_files, path + each_file + os.sep, *file_type)  # 这里参数为 *file_type 为收集参数的逆过程（即将元组解包）
        elif os.path.splitext(each_file)[1] in file_type:  # 如果文件后缀是要寻找的类型，则加入列表
            dest_files.append(path + each_file)

    return

dest_files = []
find_all_specific_type_files(dest_files, 'E:\\', '.avi', '.mp4', '.mvb')
print(dest_files)
