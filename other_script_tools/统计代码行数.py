import os
import easygui


def search_file(start_dir):
    os.chdir(start_dir)
    global target
    global source_list
    global file_list
     
    for each_file in os.listdir(os.curdir):
        if 'Windows' in each_file or 'System' in each_file or 'stdafx' in each_file or 'easygui' in each_file:
            continue
        ext = os.path.splitext(each_file)[1]
         
        if os.path.isdir(each_file):
            search_file(each_file)  # 遇见文件夹，递归搜索
            os.chdir(os.pardir)  # 递归调用结束后返回上一层目录
            
        elif ext in target:
            lines = calc_code(each_file)
            # 统计文件数
            try:
                file_list[ext] += 1
            except KeyError:
                file_list[ext] = 1
            # 统计源代码行数
            try:
                source_list[ext] += lines
            except KeyError:
                source_list[ext] = lines


def calc_code(file_name):
    lines = 0
    with open(file_name, encoding='gb18030', errors='ignore') as f:
        print('正在分析文件：%s...' % file_name)
        try:
            for each_line in f:
                lines += 1
        except UnicodeDecodeError:
            pass  # 不可避免会遇到格式不兼容的文件，这里忽略掉
    return lines


def show_result():
    global source_list
    global file_list
    lines = 0
    total = 0
    text = ''
    
    for i in source_list:
        lines = source_list[i]
        total += lines
        text += '【%s】原文件 %d 个，源代码 %d 行\n' % (i, file_list[i], lines)
    title = '统计结果'
    msg = '您目前共累计编写了 %d 行代码，完成进度： %.2f%%\n离10万行代码还差 %d 行，请继续努力！' \
          % (total, total/1000, 100000-total)
    easygui.textbox(msg=msg, title=title, text=text)


target = ['.c', '.cpp', '.py', '.java', '.cc', '.pas', '.asm', '.txt']
file_list = dict()
source_list = dict()

easygui.msgbox('请打开您存放所有代码的文件夹', '统计代码')
path = easygui.diropenbox('请选择您的代码库：')

search_file(path)
show_result()
