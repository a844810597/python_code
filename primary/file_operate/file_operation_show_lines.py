def show_lines(file_name, show_range=':'):
    file = open(r'{}'.format(file_name))
    start, end = show_range.split(':')
    if start == '':
        start = None
    else:
        start = int(start)
    if end == '':
        end = None
    else:
        end = int(end)
    for each_line in file.readlines()[start:end]:
        print(each_line)

file_name = input('Enter the file path :')
show_range = input('Enter the range of lines shown (start:end, example: 1:10) :')
show_lines(file_name, show_range)
