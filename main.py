"""
Задание №1

Задание: Написать программу, которая принимает на вход слово и проверяет, является ли оно палиндромом.
Условия:

    Программа должна быть нечувствительна к регистру.
    Игнорировать пробелы и знаки пунктуации.
Пример использования:
    isPalindrom("level") # True
    isPalindrom("hello") # False

Задание №2

Задание: Написать программу, которая принимает список слов и проверяет, какие из них являются палиндромами.
Условия:

    Слова передаются в виде списка через ввод пользователя.
    Программа должна вывести все палиндромы из списка.

Пример использования:
    isPalindromList(["hello", "list", "level"]) # ["level"]

Задание №3

Задание: Написать программу, которая ищет все палиндромы в строке текста.
Условия:

    Программа должна игнорировать регистр и знаки пунктуации.
    Если палиндромы повторяются, выводить их только один раз.

Пример использования isPalindromString("Madam, Anna went to the civic center") # ["madam", "anna", "civic"]
"""
import re


def isPalindrom(str):
    str = re.sub(r'[^A-zА-я]', '', str).lower()
    if str == ''.join(reversed(str)):
        return True
    else:
        return False

print(isPalindrom("levE l"))
print(isPalindrom("hel lo"))

def isPalindromList(list):
    res = []
    for i in list:
        str = re.sub(r'[^A-zА-я]', '', i).lower()
        if str == ''.join(reversed(str)):
            res.append(str)
        else:
            pass

    return res

print(isPalindromList(["hello", "list", "level"]))

def isPalindromString(str):
    mylist = re.sub(r'[^A-zА-я ]', '', str).lower().split(' ')
    res = []
    for i in mylist:
        if i == ''.join(reversed(i)):
            res.append(i)
        else:
            pass

    return res

print(isPalindromString("Madam, Anna went to the civic center"))