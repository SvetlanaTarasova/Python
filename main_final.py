from tkinter import *
from dictionary import *

class numbers(object):

    def __init__(self, numbers, rank):
        self.numbers = numbers
        self.rank = rank

def old_slavonic_numbers(res_number):
    i = 1
    list_res_numbers = []
    temp_txt = str(res_number) + ", "
    while res_number > 0:
        res_number, number_ = divmod(res_number, 10)
        list_res_numbers.append(number_ * i)
        i = i * 10
    i = len(list_res_numbers) - 1
    while i >= 0:
        if list_res_numbers[i] in old_slavonic_language:
            temp_txt = temp_txt + old_slavonic_language[list_res_numbers[i]]
        i = i - 1
    return temp_txt

def Eror(list_num_rank, list_num_rank2, list_num, list_num2):

    if list_num_rank.rank == 1:
        text = "Разряд единиц"
    elif list_num_rank.rank == 2:
        text = "Число формата 11-19"
    elif list_num_rank.rank == 3:
        text = "Разряд десятков"
    elif list_num_rank.rank == 4:
        text = "Разряд сотен"


    if list_num_rank2.rank == 1:
        text2 = "разрядом единиц"
    elif list_num_rank2.rank == 2:
        text2 = "числом формата 11-19"
    elif list_num_rank2.rank == 3:
        text2 = "разрядом десятков"
    elif list_num_rank2.rank == 4:
        text2 = "разрядом сотен"

    temp_txt = text + " '" + list_num + "' " + "не может стоять перед " + text2 + " '" + list_num2 + "'!"

    return temp_txt

def insert():
    flag_break = 0
    flag_break2 = 0
    res_number = 0
    flag = 0
    res_number = int(res_number)
    str_ = txt.get() + " "
    flag_null = 0
    temp_str_ = ""
    list_num = []
    list_num_rank = []
    for i in range(0, len(str_)):
        if str_[i] != " ":
            temp_str_ += str_[i]
            flag = 1
            if (str_[i + 1] == " ") and (flag == 1):
                list_num.append(temp_str_)
                temp_str_ = ""

    if len(list_num) == 0:
        flag_null = 1
    j = 0

    for i in range(0, len(list_num)):
        if list_num[i] in units:
            number = numbers(units[list_num[i]], 1)
            list_num_rank.append(number)
        else:
            if list_num[i] in tens_one:
                number = numbers(tens_one[list_num[i]], 2)
                list_num_rank.append(number)
            else:
                if list_num[i] in tens:
                    number = numbers(tens[list_num[i]], 3)
                    list_num_rank.append(number)
                else:
                    if list_num[i] in hundreds:
                        number = numbers(hundreds[list_num[i]], 4)
                        list_num_rank.append(number)
                    else:
                        j = i
                        flag_break = 1
                        break

    i = 0
    if flag_null == 1:
        lbl.configure(text="Ничего не было введено, повторите ввод!")
    elif flag_break == 1:
        res = "Слово '" + list_num[j] + "' не распознано, введите число заново!"
        lbl.configure(text=res)
    else:
        while i < (len(list_num_rank)):
            if (i + 1 < len(list_num_rank)) and list_num_rank[i].rank == 3 and list_num_rank[i + 1].rank == 2:
                flag_break2 = 1
                temp_txt = Eror(list_num_rank[i], list_num_rank[i+1], list_num[i], list_num[i+1])
                break
            elif (i + 1 < len(list_num_rank)) and list_num_rank[i].rank <= list_num_rank[i + 1].rank:
                temp_txt = Eror(list_num_rank[i], list_num_rank[i + 1], list_num[i], list_num[i + 1])
                flag_break2 = 1
                break
            elif (i + 1 < len(list_num_rank)) and list_num_rank[i].rank == 2 and   list_num_rank[i + 1].rank == 1:
                flag_break2 = 1
                temp_txt = "Разряд десятков '" + list_num[i] + "' " + "не может стоять перед разрядом единиц '" + \
                            list_num[i + 1] + "'!"
                break
            elif list_num_rank[i].rank == 1 or list_num_rank[i].rank == 2 or list_num_rank[i].rank == 3 or list_num_rank[i].rank == 4:
                res_number += list_num_rank[i].numbers
            i = i + 1

        if flag_break2 == 1:
            lbl.configure(text=temp_txt)
        else:
            lbl.configure(text=old_slavonic_numbers(res_number))

window = Tk()

window.title("Перевод чисел")
window.geometry('720x200')
lbl = Label(window, text="                                                         Введите число на русском языке", font='Arial 12')
lbl.pack(side='top', anchor=W, ipadx=4, padx=1, ipady=3, pady=3)
frame = Frame()
frame.pack(side=TOP)
txt = Entry(frame, width=50, font='Arial 12')
txt.pack(side=TOP, anchor=N, fill='x', ipadx=7, padx=150, ipady=15, pady=1)
insert_btn = Button(frame, text="Перевести", width=10, command=insert, font='Arial 12')
insert_btn.pack(side='left', ipadx=300, padx=6, ipady=5, pady=0)

frame2 = Frame()
frame2.pack(side=LEFT, fill=X)

lbl = Label(frame2, text="", font='Arial 12', bg='white', width=450)
lbl.pack(side=LEFT, anchor=W, ipadx=5, padx=5, ipady=15, pady=5)

# lbl2 = Label(window, text="Перевод на арабские и старославянские цифры :", font='Arial 12')
# lbl2.pack(side='bottom', anchor=W, ipadx=4, padx=4, ipady=3, pady=3)

window.mainloop()