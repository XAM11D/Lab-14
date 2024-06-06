# Lab-14
Лабораторна робота 14: Логічні операції в Python

Мета роботи:
Метою даної лабораторної роботи є освоєння основних логічних операцій в мові програмування Python та застосування їх для вирішення різноманітних задач. Очікуваний результат включає розуміння логічних операторів та вміння використовувати їх для побудови логічних умов.

Опис завдання:
Необхідно реалізувати кілька функцій, які демонструють застосування логічних операцій у різних контекстах. Завдання включають базові логічні перевірки, умовні оператори, логічні еквівалентності, ексклюзивне "або" (XOR), та інші.

Виконання роботи:
Кожне завдання реалізовано у вигляді окремої функції, яка приймає вхідні параметри та повертає результат. Усі функції містяться в одному файлі main.py.

Код програми:
# Task 1: Basic Boolean Operations
def check_truth(a, b, c):
    return (a and b) or c

# Task 2: Logical Equivalence
def logical_equivalence(a, b):
    return a == b

# Task 3: Exclusive Or (XOR)
def xor(a, b):
    return (a and not b) or (not a and b)

# Task 4: Conditional Greeting
def greet(condition):
    if condition:
        return "Hello, World!"
    else:
        return "Goodbye, World!"

# Task 5: Nested Conditions
def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y != z != x:
        return "All different"
    else:
        return "Neither"

# Task 7: Boolean Parity
def parity(number):
    binary_repr = bin(number)
    count_ones = binary_repr.count('1')
    return count_ones % 2 == 0

# Task 8: Majority Vote
def majority_vote(a, b, c):
    return sum([a, b, c]) > 1

# Task 9: Boolean Switch
def switch(condition):
    return not condition

# Task 10: Ternary Operator Simulation
def ternary_check(condition, if_true, if_false):
    return if_true if condition else if_false

# Task 11: Validate Combination
def validate(x, y, z):
    return x or (y and z)

# Task 12: Condition Chain
def chain_check(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"

# Task 13: Boolean Filter
def filter_true(bool_list):
    return [value for value in bool_list if value]

# Task 14: Conditional Multiplexer
def multiplexer(a, b, c, integer):
    if a:
        return integer * 2
    elif b:
        return integer * 3
    elif c:
        return integer - 5
    else:
        return integer
        
Структура проекту:
Проект організовано у вигляді папки з наступними файлами:
main.py: Основний код програми.
README.md: Файл з детальним поясненням проекту.
Опис кожного файлу та його призначення:
main.py: Містить реалізацію всіх функцій згідно з завданням.
README.md: Містить загальний опис проекту, мету, інструкції з використання та приклади використання функцій.
Опис основних функцій та методів з поясненням їх роботи:
check_truth(a, b, c): Перевіряє істинність виразу (a і b) або c.
logical_equivalence(a, b): Повертає True, якщо a і b еквівалентні.
xor(a, b): Реалізує логічну операцію виключаючий "або" (XOR).
greet(condition): Повертає "Hello, World!" якщо умова істинна, і "Goodbye, World!" якщо ні.
nested_condition(x, y, z): Перевіряє чи всі значення однакові, різні, або ні те, ні інше.
parity(number): Перевіряє парність кількості одиниць у двійковому представленні числа.
majority_vote(a, b, c): Перевіряє, чи більшість з трьох значень істинні.
switch(condition): Повертає протилежне булеве значення.
ternary_check(condition, if_true, if_false): Реалізує тернарний оператор.
validate(x, y, z): Перевіряє комбінацію умов.
chain_check(a, b, c): Перевіряє зростаючу або спадну послідовність чисел.
filter_true(bool_list): Фільтрує список булевих значень, залишаючи лише істинні.
multiplexer(a, b, c, integer): Умовний мультиплексор для маніпуляцій з числом.

Результати:
Отримані результати демонструють правильність роботи реалізованих функцій. Кожна функція повертає очікувані результати при різних вхідних даних.

Приклади виводу програми:
check_truth(True, False, True) повертає True
logical_equivalence(True, True) повертає True
xor(True, False) повертає True
greet(True) повертає "Hello, World!"
nested_condition(1, 1, 1) повертає "All same"
parity(5) повертає False (5 в двійковій формі 101, непарна кількість одиниць)
majority_vote(True, False, True) повертає True
switch(True) повертає False
ternary_check(True, "Yes", "No") повертає "Yes"
validate(False, True, True) повертає True
chain_check(1, 2, 3) повертає "Increasing"
filter_true([True, False, True]) повертає [True, True]
multiplexer(True, False, False, 10) повертає 20

Для запуску програми необхідно: Встановити Python версії 3.6 або вище.
