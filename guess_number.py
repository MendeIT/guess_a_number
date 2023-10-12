"""
Модуль игры "Угадай число".
"""

from random import randint
from sys import exit

from art import text2art
from colorama import Fore, Back, Style


def try_to_guess_number() -> str:
    """ Метод имитирующий игру 'Угадай число'."""

    number: int = randint(1, 100)
    print(Back.GREEN + 'Угадайте число от 1 до 100' + Style.RESET_ALL)
    count: int = 0

    while True:
        try:
            integer = int(input('Введите число: '))

            if integer < 1 or integer > 100:
                print(Fore.RED + 'Целое число от 1 до 100' + Style.RESET_ALL)
                continue

        except ValueError:
            print(Fore.RED + 'Введите целое число' + Style.RESET_ALL)
            continue

        else:
            count += 1
            if count == 7:
                print(Fore.YELLOW +
                      'Попробуй бинарны поиск...'
                      + Style.RESET_ALL)

            elif count == 11:
                print(Fore.YELLOW +
                      'Подсказка: Чтобы угадать число от 1 до 100, '
                      'используй деление на 2.\n Пример. 100/2 = 50, '
                      'вводим 50, далее 50/2 = 25, вводим 25...ну ты понял!'
                      + Style.RESET_ALL)

            if integer < number:
                print(Fore.RED +
                      'Ваше число меньше того, что загадано.'
                      + Style.RESET_ALL)
                continue

            elif integer > number:
                print(Fore.RED +
                      'Ваше число больше того, что загадано.'
                      + Style.RESET_ALL)
                continue

            elif integer == number:
                print(Fore.GREEN + 'Отличная интуиция! Вы угадали число :)')
                print(text2art('WIN', font="black"))
                print(f'Количество Ваших попыток: {count}')
                break


def play_again() -> None:
    """ Метод получения ответа о продолжении игры от пользователя."""

    answer = input('Введите "да" или "нет":')

    if answer in ['ДА', 'да', 'Да', 'дА']:
        try_to_guess_number()

    elif answer in ['НЕТ', 'нет', 'Нет', 'нЕт', 'нЕТ', 'неТ', 'НЕт', 'НеТ']:
        print(Back.GREEN + 'Спасибо за игру!' + Style.RESET_ALL)
        exit()

    else:
        print(Fore.RED + 'Не понял Вас =(' + Style.RESET_ALL)
        play_again()


def main():
    try:
        try_to_guess_number()
        while True:
            print(Back.GREEN + 'Хотите сыграть еще?' + Style.RESET_ALL)
            play_again()

    except KeyboardInterrupt:
        print(Back.GREEN +
              '\nЧитер! =) Сыграем в следущий раз!'
              + Style.RESET_ALL)
        exit()

    except Exception as error:
        raise error


if __name__ == "__main__":
    main()
