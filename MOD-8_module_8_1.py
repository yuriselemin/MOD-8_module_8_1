
# Домашнее задание по уроку "Try и Except".


def add_everything_up(a, b):
    try:
        num = a, b
        result = round(sum(num), 3)
        return result
    except TypeError:
        return str(a) + str(b)

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

print('----------------------------------------------------------------')

def adding_more(c, d):
    try:
        num = c, d
        result = round(sum(num), 3)
        return result
    except TypeError:
        if isinstance(c, bool) or isinstance(d, bool):
            return str(c) + str(d)
        elif c is None or d is None:
            return str(c)  + str(d)
        else:
            return str(c) + str(d)

# Примеры использования функции
print(adding_more(False, False))
print(adding_more(True, False))
print(adding_more(None, 'текст'))
print(adding_more(None, 10))
print(adding_more(None, True))



