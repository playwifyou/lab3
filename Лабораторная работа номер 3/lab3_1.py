# TODO Напишите функцию для поиска индекса товара


def index_of_item(item, item_list):
    if item in item_list:
        return item_list.index(item)
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


for find_item in ['банан', 'груша', 'персик']:
    index_item = index_of_item(find_item, items_list)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
