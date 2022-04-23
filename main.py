with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file.read().split('\n\n'):
        name, _, *args = i.split('\n')
        list_args = []
        for j in args:
            a, b, c = j.split(' | ')
            list_args.append({'ingredient_name': a, 'quantity': b, 'measure': c})
        cook_book[name] = list_args
    print(cook_book)
