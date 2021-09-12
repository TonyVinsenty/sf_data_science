'''Игра: Угадай число
Компьютер генерирует случайное целое число от 1 до 100 и алгоритм отгадывает его за наименьшее число шагов (не больше девяти).'''

import numpy as np

def number_predict(number: int = 1) -> int:
    """Функция угадывания числа.
    Реализуется путем сокращения диапазона возможных чисел в 2 раза после каждой неудачной попытки угадать.

    Args:
        number (int, optional): Загаданное случайное число. Defaults to 1.

    Returns:
        int: Число попыток.
    """
    count = 0
    median = 50 # Медиана заданного диапазона, которая будет изменяться в сторону неизвестного числа, уменьшая интервалы изменения в два раза после каждой неудачной попытки.
    
    while True:
        count += 1
        
        # Определяем разницу, которую будем вычитать или добавлять в сторону неизвестного числа, определяя ее как частное 100 и степени двойки.
        # При больших степенях двойки разница будет равна 0. В таком случае присваиваем ей 1.
        if 100 // (2**(count + 1)) != 0:
            difference = 100 // (2**(count + 1))
        else:
            difference = 1

        if median == number:
            break # Число отгадано, выход из цикла и функции
        
        elif median > number:
            median -= difference
        
        elif median < number:
            median += difference
    return count


def score_game(number_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        number_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=10000) # Список из 10000 случайных чисел для угадывания
    
    for number in random_array:
        count_ls.append(number_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Алгоритм в среднем угадывает число за {score} попыток.')

score_game(number_predict)