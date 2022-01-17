"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
print('Задание 4 \n','-'*20)

list_word4 = ['разработка', 'администрирование', 'protocol', 'standard']

for word in list_word4:
    print('Исходный вариант: ', word, type(word))
    word_byte = word.encode('utf-8')
    print('в байтах :', word_byte, type(word_byte))
    word_str = word_byte.decode('utf-8')
    print('в строке :', word_str, type(word_str))
    print('-'*20)


