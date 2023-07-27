from tkinter import *
main = Tk()


canvas = Canvas(main,height = 230, width = 200)
canvas.pack()

type_list = []
string_list = []
symbol_list = ['+','-','*','/','^','(',')','!']

operation = ''

def xfun1():
    type_list.append(int(1))
    string_list.append(str(1))
    update_new_list()
def xfun2():
    type_list.append(int(2))
    string_list.append(str(2))
    update_new_list()
def xfun3():
    type_list.append(int(3))
    string_list.append(str(3))
    update_new_list()
def xfun4():
    type_list.append(int(4))
    string_list.append(str(4))
    update_new_list()
def xfun1():
    type_list.append(int(1))
    string_list.append(str(1))
    update_new_list()
def xfun5():
    type_list.append(int(5))
    string_list.append(str(5))
    update_new_list()
def xfun6():
    type_list.append(int(6))
    string_list.append(str(6))
    update_new_list()
def xfun7():
    type_list.append(int(7))
    string_list.append(str(7))
    update_new_list()
def xfun8():
    type_list.append(int(8))
    string_list.append(str(8))
    update_new_list()
def xfun9():
    type_list.append(int(9))
    string_list.append(str(9))
    update_new_list()
def xfunplus():
    type_list.append('+')
    string_list.append('+')
    update_new_list()
def xfunminus():
    type_list.append('-')
    string_list.append('-')
    update_new_list()
def xfuntimes():
    type_list.append('*')
    string_list.append('*')
    update_new_list()
def xfundiv():
    type_list.append('/')
    string_list.append('/')
    update_new_list()
def update_new_list():
    newstring = ''.join(string_list)
    label = Label(main, text = newstring, bg ='grey')
    label.place(x=20,y = 0)
    label.pack()
def xfun0():
    type_list.append(int(1))
    string_list.append(str(1))
    update_new_list()
def reset():
    type_list.clear()
    string_list.clear()
    print(type_list)
    print(string_list)

def list_operations_simple():
    num1 = ('')
    num2 = ('')
    print(type_list)
    for element in type_list:
        if isinstance(element,int) == True:
            num1 = f'{num1}{element}'
            index = len(num1)
        elif element in symbol_list:
            if element == '+':
                type_list_copy = type_list.copy()
                type_list_copy = type_list_copy[index:]
                for element in type_list_copy:
                    if isinstance(element,int) == True:
                        num2 = f'{num2}{element}'
                operation = int(num1) + int(num2)

            elif element == '-':
                type_list_copy = type_list.copy()
                type_list_copy = type_list_copy[index:]
                for element in type_list_copy:
                    if isinstance(element,int) == True:
                        num2 = f'{num2}{element}'
                operation = int(num1) - int(num2)
            elif element == '*':
                type_list_copy = type_list.copy()
                type_list_copy = type_list_copy[index:]
                for element in type_list_copy:
                    if isinstance(element,int) == True:
                        num2 = f'{num2}{element}'
                operation = int(num1) * int(num2)
            elif element == '/':
                type_list_copy = type_list.copy()
                type_list_copy = type_list_copy[index:]
                for element in type_list_copy:
                    if isinstance(element,int) == True:
                        num2 = f'{num2}{element}'
                operation = int(num1) / int(num2)
    answer_label = Label(main, text = operation, fg = 'white', bg = 'black')
    answer_label.pack(padx = 50, pady = 7)
    answer_label.place(x=10, y=4)
    return print(operation)
button_1= Button(main, text = 1, fg='black', highlightbackground = 'black', command = xfun1)
button_1.pack(padx = 5, pady=5)
button_2= Button(main, text = 2, fg='black', highlightbackground = 'black', command = xfun2)
button_2.pack(padx = 5, pady=5)
button_3= Button(main, text = 3, fg='black', highlightbackground = 'black', command = xfun3)
button_3.pack(padx = 5, pady=5)
button_4= Button(main, text = 4, fg='black', highlightbackground = 'black', command = xfun4)
button_4.pack(padx = 5, pady=5)
button_5= Button(main, text = 5, fg='black', highlightbackground = 'black', command = xfun5)
button_5.pack(padx = 5, pady=5)
button_6= Button(main, text = 6, fg='black', highlightbackground = 'black', command = xfun6)
button_6.pack(padx = 5, pady=5)
button_7= Button(main, text = 7, fg='black', highlightbackground = 'black', command = xfun7)
button_7.pack(padx = 5, pady=5)
button_8= Button(main, text = 8, fg='black', highlightbackground = 'black', command = xfun8)
button_8.pack(padx = 5, pady=5)
button_9= Button(main, text = 9, fg='black', highlightbackground = 'black', command = xfun9)
button_9.pack(padx = 5, pady=5)
button_plus= Button(main, text = '+', fg='black', highlightbackground = 'black', command = xfunplus)
button_plus.pack(padx = 5, pady=5)
button_minus= Button(main, text = '-', fg='black', highlightbackground = 'black', command = xfunminus)
button_minus.pack(padx = 5, pady=5)
button_times= Button(main, text = '*', fg='black', highlightbackground = 'black', command = xfuntimes)
button_times.pack(padx = 5, pady=5)
button_divide= Button(main, text = '/', fg='black', highlightbackground = 'black', command = xfundiv)
button_divide.pack(padx = 5, pady=5)
button_exponent= Button(main, text = '^', fg='black', highlightbackground = 'black', command = lambda: type_list.append('^'), state = DISABLED)
button_exponent.pack(padx = 5, pady=5)
button_open_parenthesis= Button(main, text = '(', fg='black', highlightbackground = 'black', command = lambda: type_list.append('('), state = DISABLED)
button_open_parenthesis.pack(padx = 5, pady=5)
button_close_parenthesis= Button(main, text = '(', fg='black', highlightbackground = 'black', command = lambda: type_list.append(')'), state = DISABLED)
button_close_parenthesis.pack(padx = 5, pady=5)
button_factorial= Button(main, text = '!', fg='black', highlightbackground = 'black', command = lambda: type_list.append('!'), state = DISABLED)
button_factorial.pack(padx = 5, pady=5)
button_enter= Button(main, text = 'Enter', fg='black', highlightbackground = 'black', command = list_operations_simple)
button_enter.pack(padx = 5, pady=5)
button_0= Button(main, text = 0, fg='black', highlightbackground = 'black', command = xfun0)
button_0.pack(padx = 5, pady=5)
button_reset= Button(main, text = 'Reset', fg='black', highlightbackground = 'black', command = reset)
button_reset.pack(padx = 5, pady=5)
button_1.place(x=10.0, y=30)
button_2.place(x=55.0, y=30)
button_3.place(x=100.0, y=30)
button_4.place(x=10.0, y=60)
button_5.place(x=55.0, y=60)
button_6.place(x=100.0, y=60)
button_7.place(x=10.0, y=90)
button_8.place(x=55, y=90)
button_9.place(x=100, y=90)
button_plus.place(x=55, y=120)
button_minus.place(x=100, y=120)
button_times.place(x=10, y=150)
button_divide.place(x=55, y=150)
button_exponent.place(x=100, y=150)
button_open_parenthesis.place(x=10, y=180)
button_close_parenthesis.place(x=55, y=180)
button_factorial.place(x=100, y=180)
button_0.place(x=10, y=120)
button_enter.place(x=80, y=210)
button_reset.place(x=10, y=210)
main.mainloop()
