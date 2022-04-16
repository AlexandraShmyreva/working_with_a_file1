import os

with open(os.path.join(os.getcwd(), '1.txt'), encoding='utf-8') as file:
    new_list = {}
    for file in os.listdir():
        if file.endswith('.txt'):
            with open(file, encoding='utf-8') as f:
                res = len(f.readlines())
                new_list[file] = res
    list_val = list(new_list.items())
    list_val.sort(key=lambda i: i[1])
    for i in list_val:
        print(f'{i[0]}\n{i[1]}')