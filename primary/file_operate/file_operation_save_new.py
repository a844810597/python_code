def file_save_new(file_name):
    file = open(r'{}'.format(file_name), 'w')  # 打开文件
    print('Enter the content(Enter the ":w" to quit):')
    while True:  # 当输入不为':w'时，一直接受输入并写入文件
        file_content = input()
        if file_content == ':w':
            break
        else:
            file.write(file_content + '\n')
    file.close()

file_name = input('Enter the path of file :')
file_save_new(file_name)
