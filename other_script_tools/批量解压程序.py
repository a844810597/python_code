import codecs
import zipfile
import os


def search_file(file_path, *file_types):
    os.chdir(file_path)
    file_path_list = []
    
    for each_file in os.listdir(os.curdir):
        # 由于权限不够访问系统文件，故直接跳过
        if 'Windows' in each_file or 'System' in each_file or '$' in each_file:
            continue
        # 如果文件为文件夹，则进入递归搜索
        elif os.path.isdir(each_file):
            file_path_list += search_file(each_file, *file_types)
            os.chdir(os.pardir)
        # 如果文件是目标文件，则将该文件的绝对路径添加入列表
        elif os.path.splitext(each_file)[1] in file_types:
            file_path_list.append(os.getcwd() + os.path.sep + each_file)
            
    # 返回绝对路径的列表
    return file_path_list


def unzip(file_source, dest_path='E:\\FishC_Pyhton'):
    zip_file = zipfile.ZipFile(file_source, 'r')
    
    for each_file in zip_file.namelist():
        
        # 只解压我想要的文件类型
        if os.path.splitext(each_file)[1] ==  '.mp4':
            # 先将文件解压到目标目录下(dest_path)，并且将文件的路径记录下来
            # 此时我们所需要的文件(.mp4)可能在文件夹内
            old_path = zip_file.extract(each_file, dest_path)
            # 此时有编码问题，将目标文件名提取出来，重新编码解码
            file_name = os.path.basename(old_path).encode('cp437').decode('gbk')
            # 巧妙利用给文件修改路径名的方法，来将文件转移到我们需要的目标目录下(dest_path)
            os.rename(old_path, dest_path+os.path.sep+file_name)
            # 最后将原来解压出来装目标文件的空文件夹删除掉
            os.rmdir(os.path.dirname(old_path))


def del_zipfile(path):
    os.remove(path)


search_path = 'E:\\FishC_Pyhton'
file_types = ('.zip',)

for each_zipfile in search_file(search_path, *file_types):
    unzip(each_zipfile)
    #解压好后，删除掉压缩文件（可选是否进行这步操作）
    del_zipfile(each_zipfile)
    
print('解压成功！')
input('请按<Enter>键退出程序...')
