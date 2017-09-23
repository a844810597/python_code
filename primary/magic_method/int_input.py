def int_input(prompt=''):
    while True:
        try:
            int(input(prompt))
            break
        except  ValueError as reason:
            print('输入的不是一个整数,请重新输入..', '错误原因：', str(reason))

int_input('请输入一个整数：')
