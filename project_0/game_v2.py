import numpy as np

def random_predict(number:int=1) -> int:
    '''Рандомное угадывание числа. Принимает на вход число, возвращает число попыток'''
    
    count = 0
    
    while True:
        count+=1
        predict = np.random.randint(1, 101) # Предполагаем число
        if predict == number:
            break
    return count


def score_game(random_predict) -> int:
    '''Запускаем игру 1000 раз, чтобы определить среднее число попыто для угадывания заданного числа.'''
    
    count_list = []
    np.random.seed(1) # Фиксируем Random seed, чтобы эксперимент был воспроизводим.
    random_array = np.random.randint(1, 101, size=(1000)) # Список из 1000 случайных чисел
    
    for number in random_array:
        count_list.append(random_predict(number))
    
    score = int(np.mean(count_list))
    print(f'Алгоритм угадывает число в среднем за {score} попыток')
    return score 


if __name__ == '__main__':
    score_game(random_predict)