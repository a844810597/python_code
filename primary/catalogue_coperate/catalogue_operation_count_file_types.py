import os

def count_files(path = os.curdir):
    all_files = os.listdir(path)
    type_dict = dict()

    for each_file in all_files:  # 文件夹类型必须单独统计，因为没有后缀名
        if os.path.isdir(path + each_file):  # isdir 和 isfile 参数都要使用绝对路径
            type_dict.setdefault('文件夹', 0)
            type_dict['文件夹'] += 1
        else:
            ext = os.path.splitext(each_file)[1]
            type_dict.setdefault(ext, 0)
            type_dict[ext] += 1
            
    return type_dict

print(count_files('E:/'))

