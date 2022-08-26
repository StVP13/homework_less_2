in_list = input('введите слова с пробелом:').split()
for i, v in enumerate(in_list, 1):
    print(f'{i}) {v:.10}')