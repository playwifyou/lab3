# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()
    dictionary_for_numbers = {}
    for letter in text:
        if letter.isalpha():
            if letter in dictionary_for_numbers:
                dictionary_for_numbers[letter] += 1
            else:
                dictionary_for_numbers[letter] = 1
    return dictionary_for_numbers


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dictionary_for_numbers):
    number_of_letters = sum(dictionary_for_numbers.values())
    dictionary_for_frequency = {}
    for letter in dictionary_for_numbers:
        number = dictionary_for_numbers[letter]
        dictionary_for_frequency[letter] = number / number_of_letters
    return dictionary_for_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dictionary_for_numbers = count_letters(main_str)
dictionary_for_frequency = calculate_frequency(dictionary_for_numbers)
for result in dictionary_for_frequency:
    print(f"{result}: {'{:.2f}'.format(dictionary_for_frequency[result])}")