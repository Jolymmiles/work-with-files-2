from datetime import datetime

alphabet = {"А": "Андрей", "Б": "Борис", "В": "Валетин", "Г": "Галина", "Д": "Данил", "Е": "Евгений", "Ж": "Жанна",
            "З": "Захар", "И": "Иисус", "К": "Константин", "Л": "Лев", "М": "Марта", "Н": "Наталья", "О": "Олег",
            "П": "Прохор", "Р": "Рената", "С": "Снежана",
            "Т": "Тамир", "У": "Ульяна", "Ф": "Федор", "Ч": "Чарли", "Э": "Эльдар", "Ю": "Юлиан", "Я": "Яков",
            "а": "Андрей", "б": "Борис", "в": "Валетин", "г": "Галина", "д": "Данил", "е": "Евгений", "ж": "Жанна",
            "з": "Захар", "и": "Иисус", "к": "Константин", "л": "Лев", "м": "Марта", "н": "Наталья", "о": "Олег",
            "п": "Прохор", "р": "Рената", "с": "Снежана",
            "т": "Тамир", "у": "Ульяна", "ф": "Федор", "ч": "Чарли", "э": "Эльдар", "ю": "Юлиан", "я": "Яков", }
number_3 = {"0": "Ноль", "1": "Сто", "2": "Двести", "3": "Триста", "4": "Четыреста", "5": "Пятьсот",
            "6": "Шестьсот",
            "7": "Семьсот", "8": "Восемьсот", "9": "Девятьсот"}
number_2 = {"0": "Ноль", "1": "Десять", "2": "Двадцать", "3": "Тридцать", "4": "Сорок", "5": "Пятьдесят",
            "6": "Шестьдесят",
            "7": "Семьдесят", "8": "Восемьдесят", "9": "Девяносто"}
number_1 = {"0": "Ноль", "1": "Один", "2": "Два", "3": "Три", "4": "Четыре", "5": "Пять", "6": "Шесть",
            "7": "Семь", "8": "Восемь", "9": "Девять"}
digits = {"11": "Одинадцать", "12": "Двенадцать", "13": "Тринадцать", "14": "Четырнадцать", "15": "Пятнадцать",
          "16": "Шестнадцать",
          "17": "Семнадцать", "18": "Восемнадцать", "19": "Девятнадцать"}
task = int(input('Введите номер задания: '))
if task == 1:
    Flag = False
    file = open('enter.txt', mode='r')
    file_output = open('output.txt', mode='w')
    for line in file:
        if 'ФИО' in line:
            continue
        line_split = line.split('|')

        output = f'Идентификация государственного регистрационного знака:{line_split[4]}30 регион \n'
        file_output.write(output)
        print(output)

        print('( ', end='')
        Flag = False
        numbers = line_split[4]
        code = '('
        number = numbers
        for i in range(len(number)):
            # Буквы
            if number[i] in alphabet:
                print(alphabet[number[i]], end=' ')
                code = code + alphabet[number[i]] + ' '

            # Сотни
            elif i == 2:
                print(number_3[number[i]], end=' ')
                code = code + number_3[number[i]] + ' '

            # Десятки
            elif i == 3 and 10 < (int(number[3] + number[4])) < 20:
                print(digits[number[3] + number[4]], end=' ')
                code = code + digits[number[3] + number[4]] + ' '
                Flag = True
            elif i == 3:
                if number[2] == '0' and number[i] == '0':
                    print('Ноль', end=' ')
                    code = code + 'Ноль '
                elif number[i] in '123456789':
                    print(number_2[number[i]], end=' ')
                    code = code + number_2[number[i]] + ' '

            # Еденицы
            elif i == 4:
                if Flag == False:
                    if number[3] == '0' and number[2] == '0' and number[i] == '0':
                        print('Ноль', end=' ')
                        code = code + 'Ноль '
                    elif number[i] in '123456789':
                        print(number_1[number[i]], end=' ')
                        code = code + number_1[number[i]] + ' '

        code = code + '30 регион)\n'
        print('30 регион)', end='')
        file_output.write(code)
        print()

        output_last = f'Получатель: Банк России \n' \
                      f'Плательщик: {line_split[0]} \n' \
                      f'Адресс: {line_split[5]} \n' \
                      f'Постановление (УИН): 12354984654798 \n' \
                      f'Вид платежа: Штраф за нарушение ПДД \n' \
                      f'Дата: 20.04.2018 \n' \
                      f'Сумма:{line_split[9]}'
        print(output_last, end='')
        file_output.write(output_last)
        split_date = line_split[3].split('.')
        first_date = datetime(int(split_date[2]), int(split_date[1]), int(split_date[0]))
        stage_driver = (datetime.now() - first_date).days
        stage_driver = stage_driver / 365
        stage_driver = str(stage_driver).split('.')
        task4 = f'Водительский стаж: {stage_driver[0]}\n'
        print(task4)
        file_output.write(task4)
        split_date_old = line_split[1].split('.')
        if int(split_date_old[0]) > 3:
            split_date_old[0] = int(split_date_old[0]) - 2
        second_date = datetime(int(split_date_old[2]), int(split_date_old[1]), int(split_date_old[0]))
        years_old = (datetime.now() - second_date).days
        years_old = years_old / 365
        years_old = str(years_old).split('.')
        task5 = f'Возраст водителя: {years_old[0]} лет \n'
        print(task5)
        file_output.write(task5)
        print()

        task_data_na = 'Дата нарушения: 29.04.2021\n'
        file_output.write(task_data_na)

        cost = line_split[9].split(' ')
        cost = int(cost[1])
        task6 = f'Сумма выплат: {cost} \n\n'
        file_output.write(task6)

    file.close()
    file = open('enter.txt', mode='r')
    file_sorted = open('sorted.txt', mode='w')

    data_base = []
    for lines in file:
        line1 = lines.split('|')
        if 'ФИО' in line1[0]:
            continue
        data_base.append(lines)

    violation = []
    for i in data_base:
        i = i.split('|')
        if i[8] not in violation:
            violation.append(i[8])

    for i in violation:
        file_sorted.write(f'----------------------------------------------------\n'
                          f'Нарушение: {i}\n')
        for line in data_base:
            line = line.split('|')
            if line[8] == i:
                split_date = line[3].split('.')
                first_date = datetime(int(split_date[2]), int(split_date[1]), int(split_date[0]))
                stage_driver = (datetime.now() - first_date).days
                stage_driver = str(stage_driver / 365).split('.')

                line_split9 = line[9].split(' ')
                cost = int(line_split9[1])
                if int(stage_driver[0]) > 5:
                    cost = cost - cost / 100 * 10
                elif int(split_date[0]) > 10:
                    cost = cost - cost / 100 * 20
                elif int(split_date[0]) > 20:
                    cost = cost - cost / 100 * 30
                elif int(split_date[0]) < 1:
                    cost = cost + cost / 100 * 10

                output_text = f'Фамилия И.О: {line[0]}\n' \
                              f'Номер водительского удостоверения: {line[2]}\n' \
                              f'Стаж: {stage_driver[0]} лет\n' \
                              f'Гос. номер: {line[4]}\n' \
                              f'Штраф: {cost}\n\n'
                file_sorted.write(output_text)
elif task == 2:

    MonthDict = {1: "Январь",
                 2: "Февраль",
                 3: "Март",
                 4: "Апрель",
                 5: "Май",
                 6: "Июнь",
                 7: "Июль",
                 8: "Август",
                 9: "Сентябрь",
                 10: "Октябрь",
                 11: "Ноябрь",
                 12: "Декабрь"
                 }

    file_base_2 = open('База2.txt', mode='r', encoding='utf-8')
    data_base_2 = []
    for line in file_base_2:
        data_base_2.append(line)
    new_file_2 = open('Сводная таблица.txt', mode='w', encoding='utf-8')
    for ik in data_base_2:
        new_file_2.write(ik)
    sorted_date_base = []
    for k in data_base_2:
        if k != 'Дата|Товар|Выручка\n':
            splited_line = k.split(' ')[0]
            sorted_date_base.append(splited_line)
    sorted_date_base = sorted(sorted_date_base, key=lambda d: datetime.strptime(d, '%d.%m.%Y'))
    file_sorted_base_2 = open('Соритрованный по дате.txt', mode='w', encoding='utf-8')
    file_sorted_base_2.write('Дата|Товар|Выручка\n')
    for i in range(len(sorted_date_base)):
        for l in range(len(data_base_2)):
            split_l = data_base_2[l].split(' ')[0]
            split_l = split_l
            if sorted_date_base[i] == split_l and data_base_2[l] != 'Дата|Товар|Выручка\n':
                file_sorted_base_2.write(data_base_2[l])

    file_rate = open('Сортировка по рейтингу.txt', mode='w', encoding='utf-8')
    clean_base_2 = []
    for i in data_base_2[1:]:
        if i.split(' ')[0] not in clean_base_2:
            clean_base_2.append(i.split(' ')[0])

    rate_array = []
    for date in range(len(clean_base_2)):
        date_products = [clean_base_2[date]]

        for k in data_base_2:
            if clean_base_2[date] == k.split(' ')[0]:
                k = k.replace('\n', '')
                date_products.append(k[11:])
        rate_array.append(date_products)
    rate_sort = []
    for i in rate_array:
        sorted_date = sorted(i[1:], key=lambda cost: int(cost.split(' ')[1]), reverse=False)
        sorted_date.append(i[0])
        rate_sort.append(sorted_date[::-1])

    for i in rate_sort:
        str = f'Дата: {i[0]} '
        for k in i[1:]:
            str += k + ' '
        str = str + '\n'
        file_rate.write(str)

    money_array = []
    arrat_check = []
    for i in rate_sort:
        if i[0][3:5] not in arrat_check:
            arrat_check.append(i[0][3:5])
            summa = 0
            for k in rate_sort:
                if i[0][3:5] == k[0][3:5]:
                    for money in k[1:]:
                        summa += int(money.split(' ')[1])
            string = i[0] + f' {summa}'
            money_array.append(string)
    money_array_sorted = sorted(money_array, key=lambda cost: int(cost.split(' ')[1]))

    print(
        f'Максимально прибыльный месяц: {MonthDict[int(money_array_sorted[len(money_array_sorted) - 1].split(" ")[0][3:5])]}. Прибыль составила: {money_array_sorted[len(money_array_sorted) - 1].split(" ")[1]}')
    print(
        f'Минимально прибыльный месяц: {MonthDict[int(money_array_sorted[0].split(" ")[0][3:5])]}. Прибыль составила: {money_array_sorted[0].split(" ")[1]}')

    arrat_check_2 = []
    money_days = []
    for i in rate_sort:
        if i[0] not in arrat_check_2:
            arrat_check_2.append(i[0])
            summa = 0
            for k in rate_sort:
                if i[0] == k[0]:
                    for money in k[1:]:
                        summa += int(money.split(' ')[1])
            string = i[0] + f' {summa}'
            money_days.append(string)

    real_days = []

    for i in range(1, 26):
        if i < 10:
            str = f'0{i}'
            real_days.append(str)
        else:
            real_days.append(i)
    real_month = []
    for i in range(1, 13):
        if i < 10:
            str = f'0{i}'
            real_month.append(str)
        else:
            real_month.append(i)

    print('День     ', end='')
    for i in range(1, 26):
        print(i, end='\t')
    print()
    for month in range(1, len(real_month)):
        len_word = ' ' * (9 - len(MonthDict[month]))
        print(MonthDict[month], end=len_word)
        for day in real_days:
            str = f'{day}.{real_month[month]}.2001'
            if str in arrat_check_2:
                for i in money_days:
                    if i.split(' ')[0] == str:
                        print(i.split(' ')[1], end='\t')
            else:
                print('0', end='\t')
        print()
