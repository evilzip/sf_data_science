"""Игра угадай число
Компьютер сам загадывает и сам угадывает число"""
import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # пердполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def smart_predict(number: int) -> int:
    """Угадывает число методом деления диапазона поиска пополам

    Args:
        number (int): Число которое нужно угадать

    Returns:
        int: число попыток
    """
    count = 0
    max_number = 101  # начальный "правая" граница диапазона поиска
    min_number = 0  # начальная "левая граница" диапазона поискаc
    while True:
        count += 1
        # проверяем лежит ли искомое число посередине текущего диапазона
        if number == (max_number+min_number) // 2:
            break
        # если число меньше центрального значения диапазона, то сдвигаем правую границу влево на половину
        elif number < (max_number+min_number) // 2:
            # новое значение правой границы нового дипазона поиска
            max_number = (max_number+min_number) // 2
        # если число больше центрального значения диапазона, то сдвигаем левую границу вправо на половину
        elif number > (max_number+min_number) // 2:
            # новое значени левой границы нового диапазона поиска
            min_number = (max_number+min_number) // 2
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подхов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        1, 101,  size=(1000))  # Загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return score


if __name__ == '__main__':
    print(score_game(random_predict))
    print(score_game(smart_predict))
