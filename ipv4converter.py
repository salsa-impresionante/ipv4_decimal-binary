from tkinter import *
from tkinter import ttk
from tkinter import messagebox

main = Tk()
main.title("IPv4 Converter v1.3")

def start_convert():
    ask1 = str(oct1.get())
    if len(ask1) < 4:
        from_dec()
    elif len(ask1) ==8:
        from_bin()
    else:
        messagebox.showinfo(title = 'Error', message = 'You have entered a number\nthat is not an IPv4 address!')

def from_dec():
    ask1 = int(oct1.get())
    ans1 = f'{ask1:08b}'

    ask2 = int(oct2.get())
    ans2 = f'{ask2:08b}'

    ask3 = int(oct3.get())
    ans3 = f'{ask3:08b}'

    ask4 = int(oct4.get())
    ans4 = f'{ask4:08b}'

    binary.configure(state='normal')
    binary.delete('1.0', END)
    binary.insert(END, ans1)
    binary.insert(END, '.')
    binary.insert(END, ans2)
    binary.insert(END, '.')
    binary.insert(END, ans3)
    binary.insert(END, '.')
    binary.insert(END, ans4)
    binary.configure(state='disabled')


def from_bin():
    ask = str(oct1.get())
    last = []
    ans = []
    multiplier = [128, 64, 32, 16, 8, 4, 2, 1]
    for each in ask:
        ans.append(int(each))
    for num1, num2 in zip(ans, multiplier):
        last.append(num1 * num2)
    ans1 = sum(last)

    ask = str(oct2.get())
    last = []
    ans = []
    for each in ask:
        ans.append(int(each))
    for num1, num2 in zip(ans, multiplier):
        last.append(num1 * num2)
    ans2 = sum(last)

    ask = str(oct3.get())
    last = []
    ans = []
    for each in ask:
        ans.append(int(each))
    for num1, num2 in zip(ans, multiplier):
        last.append(num1 * num2)
    ans3 = sum(last)

    ask = str(oct4.get())
    last = []
    ans = []
    for each in ask:
        ans.append(int(each))
    for num1, num2 in zip(ans, multiplier):
        last.append(num1 * num2)
    ans4 = sum(last)


    binary.configure(state='normal')
    binary.delete('1.0', END)
    binary.insert(END, ans1)
    binary.insert(END, '.')
    binary.insert(END, ans2)
    binary.insert(END, '.')
    binary.insert(END, ans3)
    binary.insert(END, '.')
    binary.insert(END, ans4)
    binary.configure(state='disabled')

enter_frame = ttk.LabelFrame(main, text='Enter IP Adress (Decimal or Binary):')
enter_frame.pack(fill="both", expand="yes")
enter_frame.config(padding=(40, 10))

out_frame = ttk.LabelFrame(main, text='Here is the conversion:')
out_frame.pack(fill="both", expand="yes")
out_frame.config(padding=(40, 10))

run_frame = ttk.Frame(main)
run_frame.pack(fill="both", expand="yes")
run_frame.config(padding=(40, 10))

copy_frame = ttk.Frame(main)
copy_frame.pack(fill="both", expand="yes")

Label(copy_frame, text=" MIT GitHub salsa-impresionante ").pack()

oct1 = ttk.Entry(enter_frame, width=8)
oct1.grid(row=0, column=0)

l1 = Label(enter_frame, text='  .  ')
l1.grid(row=0, column=1)

oct2 = ttk.Entry(enter_frame, width=8)
oct2.grid(row=0, column=2)

l2 = Label(enter_frame, text='  .  ')
l2.grid(row=0, column=3)

oct3 = ttk.Entry(enter_frame, width=8)
oct3.grid(row=0, column=4)

l3 = Label(enter_frame, text='  .  ')
l3.grid(row=0, column=5)

oct4 = ttk.Entry(enter_frame, width=8)
oct4.grid(row=0, column=6)

binary = Text(out_frame, width=35, height=1)
binary.configure(state='disabled')
binary.pack()

Button(run_frame, text='               Quit               ',
       command=main.destroy).grid(row=0, column=3, sticky=W, pady=4)
Button(run_frame, text='               Show               ',
       command=start_convert).grid(row=0, column=0, sticky=W, pady=4)

mainloop()
