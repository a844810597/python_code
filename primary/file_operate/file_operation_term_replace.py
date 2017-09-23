def file_replace_term(file_name, rep_word, new_word):
    file = open(r'{}'.format(file_name), 'r')  # 先只读的方式打开
    string = file.read()  # 将整个文件内容已字符串的形式付给string
    count_word = string.count(rep_word)  # 统计有多少个待替换的词
    decision = (input('确定将{count}个{rep}全部替换成{new}吗？(Yes/No)\n'\
                      .format(count=count_word,rep=rep_word,new=new_word))).lower()
    file.close()  # 关闭只读的方式
    if decision == 'yes':
        file = open(r'{}'.format(file_name), 'w')  # 已只写的方式打开
        file.write(string.replace(rep_word, new_word))
        print('替换成功!')
        file.close()
        return 1
    else:
        return 0

file_name = input('Enter the file path :')
rep_word = input('Enter the replaced word :')
new_word = input('Enter the new word :')
file_replace_term(file_name, rep_word, new_word)
