def decimal_to_binary(n):
    result = ''
    if n // 2 ==0:
        result = result + str(n % 2) #  加数的顺序不能颠倒
        return result
    else:
        temp = str(n % 2)
        return decimal_to_binary(n // 2) + temp #  加数的顺序不能颠倒

n = int(input('请输入十进制数:'))
print(decimal_to_binary(n))
input("按任意键结束程序...")
