import easygui


title = '用户注册系统'
fields = ('*真实姓名', '*手机号码', '*QQ', 'E-mail', '*用户名', '*密码')
values = ()

easygui.msgbox(msg='欢迎进入用户注册系统！', title=title)
values = easygui.multpasswordbox(msg='带 * 号的选项为必填', title=title,
                        fields=fields)

while True:
    if values == None:
        break
    errmsg = ''
    for i in range(len(fields)):
        neccessarity = fields[i].strip()
        if values[i].strip() == '' and neccessarity[0] == '*':
            errmsg += ("%s为必填项。\n" % neccessarity)
    easygui.msgbox(msg=errmsg)
    if errmsg == '':
        easygui.msgbox(msg='恭喜您，注册成功！', title=title)
        break
    values = easygui.multpasswordbox(msg='带 * 号的选项为必填', title=title,
                        fields=fields)

print('用户资料如下：%s' % str(values))


