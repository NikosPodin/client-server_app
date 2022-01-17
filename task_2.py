"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
print('Задание 2 \n','-'*20)
list_word3 = ["class", "function", "method"]
for word in list_word3:
    word_new = 'b'+f"'{word}'"
    print(type(word_new),',', word_new,',', len(word_new)-3,'\n')

#Либо
list_word3_1 = [
    b"class",
    b"function",
    b"method"]
for list in list_word3_1:
    print(type(list), list, len(list))
