import random
import easygui

secret = random.randint(0, 100)  # 生成0~100的随机数
title = '猜数字小游戏'

easygui.msgbox(msg='欢迎进入猜数字小游戏~', title=title, ok_button='进入游戏')
guess = easygui.integerbox(msg='猜猜看，我现在心里想的是哪个数字哦？（0~100）',title=title, upperbound=100)
count = 1

while guess != secret:
    if guess > secret:
        guess = easygui.integerbox(msg='猜大了哦，再试试看？',title=title, upperbound=100)
    else:
        guess = easygui.integerbox(msg='猜小了哦，再试试看？',title=title, upperbound=100)
    count += 1

easygui.msgbox(msg='恭喜你，猜对了哦！'+'一共用了'+str(count)+'次')
