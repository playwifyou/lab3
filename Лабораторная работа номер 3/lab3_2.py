# TODO Напишите функцию find_common_participants


def find_common_participants(first_group, second_group, separator=","):
    first_group_set = set(first_group.split(separator))
    second_group_set = set(second_group.split(separator))
    return sorted(list(first_group_set.intersection(second_group_set)))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
