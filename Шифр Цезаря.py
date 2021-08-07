abc_ru = [chr(i) for i in range(ord('а'), ord('я') + 1)]
ABC_RU = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
abc_en = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ABC_EN = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

def check_text(txt, lng):
    for i in txt:
        if lng == '1' and i.isalpha() and i not in abc_en and i not in ABC_EN:
            return False
        elif lng == '2' and i.isalpha() and i not in abc_ru and i not in ABC_RU:
            return False
    else:
        return True

def CeasarCode() :
    print('Добро пожаловать в программу "Шифр Цезаря"!\nВыберете нужный Вам режим:', '1 - шифрование', '2 - дешифрование', '3 - взлом шифра без пароля', sep='\n')
    while True:
        task = input()
        if task != '1' and task != '2' and task != '3':
            print('Пожалуйста, введите цифру "1", "2" или "3" для выбора режима:\n1 - шифрование\n2 - дешифрование\n3 - взлом шифра без пароля\n')
        else:
            break
    if task == '1':
        print('Режим "шифрования" активирован!')
    elif task == '2':
        print('Режим "дешифрования" активирован!')
    else:
        print('Режим взлома активирован!')
    print('Выберите алфавит кодировки для работы:', '1 - латиница', '2 - кириллица', sep='\n')
    while True:
        language = input()
        if language != '1' and language != '2':
            print('Пожалуйста, введите корректные данные:\n')
        else:
            break
    print('Введите текст:')
    while True:
        text = input()
        if check_text(text, language):
            break
        else:
            print('Текст не соответствует выбранному языку ввода. Попробуйте еще раз!')
    if task != '3':
        print('Введите пароль - шаг сдвига вправо')
        while True:
            shift = input()
            if not shift.isdigit():
                print('Пожалуйста, введите целое положительное число:\n')
            else:
                shift = int(shift)
                break 
    elif task == '3':
        print('Выберите подходящий вариант из представленных ниже расшифровок:')
        shift = None
    new_text = ''

    def main(task, language, text, shift, new_text) :
        if language == '1':
            borders = ['a', 'A', 'z', 'Z']
            total = 26
            abc_low = abc_en
            abc_high = ABC_EN
        elif language == '2':
            borders = ['а', 'А', 'я', 'Я']
            total = 32
            abc_low = abc_ru
            abc_high = ABC_RU
        if task == '1':
            for i in text:
                if i.isalpha():
                    if i in abc_low and ord(i) + shift <= ord(borders[2]):
                        new_text += chr(ord(i) + shift)
                    elif i in abc_high and ord(i) + shift <= ord(borders[3]):
                        new_text += chr(ord(i) + shift)
                    else:
                        new_text += chr(ord(i) + shift - total)
                else:
                    new_text += i
        elif task == '2':
            for i in text:
                if i.isalpha():
                    if i in abc_low and ord(i) - shift >= ord(borders[0]):
                        new_text += chr(ord(i) - shift)
                    elif i in abc_high and ord(i) - shift >= ord(borders[1]):
                        new_text += chr(ord(i) - shift)
                    else:
                        new_text += chr(ord(i) - shift + total)
                else:
                    new_text += i
        elif task == '3':
            for j in range(1, len(abc_low) + 1):
                new_text = ''
                for i in text:
                    if i.isalpha():
                        if i in abc_low and ord(i) - j >= ord(borders[0]):
                            new_text += chr(ord(i) - j)
                        elif i in abc_high and ord(i) - j >= ord(borders[1]):
                            new_text += chr(ord(i) - j)
                        else:
                            new_text += chr(ord(i) - j + total)
                    else:
                        new_text += i
                print('Шаг сдвига = ', j, '||', 'зашифрованный текст - ', new_text)         
        if task != '3':
            print('----------------------------\nРезультат обработки текста: = ', new_text,'\n----------------------------')

    main(task, language, text, shift, new_text)

CeasarCode()
while True:
    print()
    q = input('Хотите продолжить?\nВведите 1 для повторного запуска программы\nВведите 2 для выхода из программы\n')
    if q not in '1, 2':
        print('Пожалуйста, введите цифру "1" для повтора или цифру "2" для выхода!\n')
    elif q == '1':
        CeasarCode()
    else:
        break
