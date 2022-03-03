# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

eng_rus = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def translate(eng_word):
    return eng_rus.get(eng_word)


print(translate('zero'))
print(translate('five'))