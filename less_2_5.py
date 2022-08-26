my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1,]
new_number = ''
while new_number != 'q':
    i = 0
    new_number = input('введите новый элемент рейтинга натуральных чисел.\n для выхода - q\n')
    if new_number.isdigit():
        for n in my_list:
            if int(new_number) <= n:
                i += 1
            else:
                break
        my_list.insert(i, int(new_number))
    print(my_list)