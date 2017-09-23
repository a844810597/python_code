import os
import easygui


path = easygui.fileopenbox(filetypes = ['*.txt'])  # 选择要打开的文件路径
with open(path, 'r') as file:
    sour_text = file.read()
    return_text = easygui.textbox(msg='文件{}的内容如下'.format(path), title='显示文件内容',
                    text=sour_text)[:-1]
    # textbox返回的文本会在末尾附加一个 \n，所以此处要去掉附加的 \n
        
if sour_text != return_text:  # 如果文本发生了改变，则引发保存操作
    choice = easygui.buttonbox(msg='检测到文件内容发生改变，请选择以下操作：',
                               title='警告', choices=('覆盖保存','另存为','放弃保存'))
    if choice == '覆盖保存':
        with open(path, 'w') as file:
            file.write(return_text)
    elif choice == '另存为':
        save_path = easygui.filesavebox(title='另存为', default='text.txt', filetypes=['*.txt'])
        try:
            with open(save_path, 'x') as file:  # 已'x'的打开方式会先判断是否存在该文件，若存在则报FileExitError
                file.write(return_text)
        except OSError:  # 如果报错则说明已选择覆盖文件的操作，则重新以'w'的打开方式覆盖原文件
            with open(save_path, 'w') as file:
                file.write(return_text)
    else:
        pass
