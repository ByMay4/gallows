import os
import random
clear = lambda: os.system('cls')

print("Привет!, я загадал слово, сможешь его разгадать?")
input('*Нажми Enter, чтобы начать!*')
clear()
print("Начали!")
words = ['пирожок', 'чебурек', 'огурец', 'сосиска', 'котик', 'квокка', 'корабль', 'самолет', 'автомобиль', 'дерижабль']
word = random.choice(words)

letters = []
IsWin = True
hp = 10

while hp > 0:
    IsWin = True

    for symb in word:
        if symb in letters:
            print(symb, end=' ')
        else:
            print('*', end=' ')
            IsWin = False
    print()

    if IsWin:
        print('Ты угадал! Молодец!')
        break

    letter = input('Введите букву: ')
    letters.append(letter)
    clear()

    if letter not in word:
        hp -= 1
        print(f'Осталось попыток: {hp}')

if hp == 0:
    print('Ты проиграл! Кончились попытки')