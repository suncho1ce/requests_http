import os
from operator import itemgetter

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for dish_name in file:
        dish = dish_name.strip()
        size = file.readline()
        ingridients = []
        for count in range(int(size)):
            row = file.readline().strip().split(' | ')
            names = ['ingredient_name', 'quantity', 'measure']
            ingridients.append(dict(zip(names, row)))
        cook_book[dish] = ingridients  # добавляем новый блок с блюдом в основной словарь
        file.readline()  # пропускаем пустую строку и переходим к следующему блюду
print('Задача №1:')
print(cook_book)
print()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for i1 in cook_book[dish]:
                ingridient_details = {}
                if i1.get('ingredient_name') not in shop_list.keys():
                    ingridient_details['measure'] = i1.get('measure')
                    ingridient_details['quantity'] = int(i1.get ('quantity')) * person_count
                    shop_list[i1.get('ingredient_name')] = ingridient_details
                else:
                    just_add_quantity = int(i1.get('quantity')) * person_count
                    shop_list[i1.get('ingredient_name')]['quantity'] += just_add_quantity
        else:
            print('Какого-то блюда нет в списке, подсчёт невозможен.')
            return 'Ошибка'
    print('Задача №2:')
    print(shop_list)


get_shop_list_by_dishes(['Омлет', 'Омлет', 'Фахитос'], 3)
print()

# Задание 3

files_dir = 'task3'
root_path = os.getcwd()

task3_path = os.path.join(root_path, files_dir)
task3_list = []

for task3_file in os.listdir(task3_path):
    with open(os.path.join(task3_path, task3_file), encoding='utf-8') as task3_opened_file:
        text = task3_opened_file.read()
        lines = sum(1 for i in open(os.path.join(task3_path, task3_file), encoding='utf-8'))
        task3_list.append([task3_file, lines, text])

sorted_task3_list = sorted(task3_list, key = itemgetter(1))

print('Отсортированный по количеству строк список списков из задачи №3:')
print(sorted_task3_list)

if(os.path.isfile('task3_result.txt')):
    os.remove('task3_result.txt')

with open ('task3_result.txt', 'a+', encoding='utf-8') as result_file:
    for row in sorted_task3_list:
        for element in row:
            result_file.write(str(element) + '\n')