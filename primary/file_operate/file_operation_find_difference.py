def file_find_difference(file_name_1, file_name_2):
    file_1 = open(r'{}'.format(file_name_1))
    file_2 = open(r'{}'.format(file_name_2))
    count_lines = 0  # 数行数
    difference = []  # 记录不一样的行号
    for each_line_1, each_line_2 in zip(file_1,file_2):
        count_lines += 1
        if each_line_1 != each_line_2:
            difference.append(count_lines)
    file_1.close()
    file_2.close()
    return difference

file_name_1 = input('Enter the first file name :')
file_name_2 = input("Enter the second file name :")
difference = file_find_difference(file_name_1, file_name_2)
print('There is totally {} different lines :'.format(len(difference)))
for i in range(len(difference)):
    print('line {}'.format(difference[i]))

