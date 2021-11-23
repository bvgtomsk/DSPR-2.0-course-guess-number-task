"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Инициализируем счетчик попыток угадывания
    # Устанавливаем верхнюю и нижнюю границы диапазона угадывания (исключены из диапазона)
    lower_bound = 0
    upper_bound = 101
    
    while True:
        count += 1
        # Начинаем угадывать
        predict_number = lower_bound + (upper_bound - lower_bound) // 2 # выбираем число для угадывания посередине диапазона
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            lower_bound = predict_number # Если больше, то нижней границей диапазона становится то число, которое мы называли
        else:
            upper_bound = predict_number # Если меньше, то верхней границей диапазона становится то число, которое мы называли
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
