# числа
word_n = {
    0: "",
    1  : "один",
    2  : "два",
    3  : "три",
    4  : "четыре",
    5  : "пять",
    6  : "шесть",
    7  : "семь",
    8  : "восемь",
    9  : "девять",
    10 : "десять",
    11 : "одиннадцать",
    12 : "двенадцать",
    13 : "тринадцать",
    14 : "четырнадцать",
    15 : "пятнадцать",
    16 : "шестнадцать",
    17 : "семнадцать",
    18 : "восемнадцать",
    19 : "девятнадцать"
}
# исключения
word_exc = {
    0: "",
    1: "одиннадцать",
    2: "двеннадцать",
    3: "тринадцать",
    4: "четырнадцать",
    5: "пятнадцать",
    6: "шестнадцать",
    7: "семнадцать",
    8: "восемнадцать",
    9: "девятнадцать"
}
# десятки
word_dec = {
    0: "",
    1: "десять",
    2: "двадцать",
    3: "тридцать",
    4: "сорок",
    5: "пятьдесят",
    6: "шестьдесят",
    7: "семьдесят",
    8: "восемьдесят",
    9: "девяносто"

}
# сотни
word_hund = {
    0: "",
    1: "сто",
    2: "двести",
    3: "триста",
    4: "четыреста",
    5: "пятьсот",
    6: "шестьсот",
    7: "семьсот",
    8: "восемьсот",
    9: "девятьсот"
}
# порядки
word_title = {
    1 : "тысяч",
    2 : "миллион",
    3 : "миллиард",
    4 : "триллион",
    5 : "квадриллион",
    6 : "квинтиллион",
    7 : "секстиллион",
    8 : "септиллион",
    9 : "октиллион",
    10: "нониллион",
    11: "дециллион",
    12: "ундециллион",
    13: "дуодециллион",
    14: "тредециллион",
    15: "кваттуордециллион",
    16: "квиндециллион"
}


def num2rus(number_source):
    n = number_source

    # проверка на ноль
    if number_source == 0:
        return "ноль"
    # проверка на максимальное число
    if number_source >= 1000000000000000000000000000000000000000000000000000:
        return "!!!Слишком большое число!!!"

    s_list = []
    f_list = []

    p = 1

    # разбить число по 3 цифры и записать в список и через 1 ставим "!" (порядок)
    while n // 1000 > 0:
        s_list.insert(0,"{0:0>3}".format(str(n%1000)))
        s_list.insert(0,"!" + str(p))
        n = n//1000
        p += 1
    s_list.insert(0,"{0:0>3}".format(str(n%1000)))

    # проставляем порядок там где !
    for i in range(0,len(s_list)):
        if s_list[i][0] == "!":
           s_list[i] = "!" + word_title[int(s_list[i][1:])]
           if int(s_list[i-1]) == 0:
              s_list[i] = "!"
           elif int(s_list[i-1][1:]) >= 5 and int(s_list[i-1][1:]) <= 20:
               s_list[i] += "ов"
           elif int(s_list[i-1][-1]) >= 2 and int(s_list[i-1][-1]) <= 4:
               s_list[i] += "а"
           elif int(s_list[i-1][-1]) == 1:
               pass
           elif int(s_list[i-1][-1]) == 0:
               s_list[i] += "ов"
           elif int(s_list[i-1][-1]) >= 5 and int(s_list[i-1][-1]) <= 9:
               s_list[i] += "ов"

    # исправляем тысячи
    if number_source >= 1000:
       s_list[-2] = "!" + word_title[1]
       if int(s_list[-3]) == 0:
           s_list[-2] = "!"
       elif int(s_list[-3][1:]) >= 5 and int(s_list[-3][1:]) <= 20:
           s_list[-2] = "!" + word_title[1]
       elif int(s_list[-3][-1]) >= 2 and int(s_list[-3][-1]) <= 4:
           s_list[-2] = "!" + word_title[1] + "и"
       elif int(s_list[-3][-1]) == 1:
           s_list[-2] = "!" + word_title[1] + "а"
       elif int(s_list[-3][-1]) >= 5 and int(s_list[-3][-1]) <= 9:
           s_list[-2] = "!" + word_title[1]

    # перевод цифр в слова
    for i in range(0,len(s_list)):
        if s_list[i][0] != "!":
            f_list.append(word_hund[int(s_list[i][0])])
            f_list.append(word_dec[int(s_list[i][1])])
            f_list.append(word_n[int(s_list[i][2])])
            if int(s_list[i][1:]) >= 5 and int(s_list[i][1:]) <= 19:
                f_list[-1] = word_n[int(s_list[i][1:])]
                f_list[-2] = ""
        if s_list[i][0] == "!":
            f_list.append(s_list[i][1:])

    # удаляем пробелы
    while "" in f_list:
        f_list.remove("")

    # исправляем один/две тысячи
    for i in range(0,len(f_list)):
        if f_list[i][0:5] == "тысяч":
            if f_list[i-1] == "один":
                f_list[i-1] = "одна"
            if f_list[i-1] == "два":
                f_list[i-1] = "две"

    result = " ".join(f_list)
    return result


if __name__ == "__main__":
    while True:
        number_source = input("Введите число: ")

        if number_source.isdigit() == False:
            print ("Конец программы")
            break
        else:
            number_source = int(number_source)
            print (num2rus(number_source))