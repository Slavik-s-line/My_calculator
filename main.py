import tkinter as tk

window = tk.Tk()
window.title("Calculator \U0001F9E0")
window.resizable(width=False, height=False)

# --------------------------------------------------
user_input = tk.StringVar()
expression = ""


def clear():
    global expression
    expression = ""
    user_input.set(expression)


def bt_equal():
    global expression
    try:
        result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
        user_input.set(result)
    except ZeroDivisionError:
        expression = "\U000026D4Ділення на 0"
        user_input.set(expression)


def btn_click(item):
    global expression
    expression = expression + str(item)
    user_input.set(expression)


# --------------------------------------------------

frame_result = tk.Frame(window, relief=tk.SUNKEN, borderwidth=5)
frame_result.pack()

entry_result = tk.Entry(master=frame_result, textvariable=user_input, width=18)
entry_result.pack()

# --------------------------------------------------

frame_btns_1 = tk.Frame(window)
frame_btns_1.pack()

btn_1 = tk.Button(frame_btns_1, fg="red", text="C", command=clear)
btn_1.pack(side=tk.LEFT)
btn_2 = tk.Button(frame_btns_1, text="( ", command=lambda: btn_click("("))
btn_2.pack(side=tk.LEFT)
btn_3 = tk.Button(frame_btns_1, text=" )", command=lambda: btn_click(")"))
btn_3.pack(side=tk.LEFT)
btn_4 = tk.Button(frame_btns_1, text="/", command=lambda: btn_click("/"))
btn_4.pack(side=tk.LEFT)

# --------------------------------------------------
list2 = ["7", "8", "9", "*"]

frame_btns_2 = tk.Frame(window)
frame_btns_2.pack()

for i in range(4):
    tk.Button(frame_btns_2, text=list2[i], command=lambda i=i: btn_click(list2[i])).pack(side=tk.LEFT)

# --------------------------------------------------
list3 = ["4", "5", "6", "-"]

frame_btns_3 = tk.Frame(window)
frame_btns_3.pack()

for i in range(4):
    tk.Button(frame_btns_3, text=list3[i], command=lambda i=i: btn_click(list3[i])).pack(side=tk.LEFT)

# --------------------------------------------------
list4 = ["1", "2", "3", "+"]

frame_btns_4 = tk.Frame(window)
frame_btns_4.pack()

for i in range(4):
    tk.Button(frame_btns_4, text=list4[i], command=lambda i=i: btn_click(list4[i])).pack(side=tk.LEFT)

# --------------------------------------------------
frame_btns_5 = tk.Frame(window)
frame_btns_5.pack()

btn_1 = tk.Button(frame_btns_5, text="      0       ", command=lambda: btn_click("0"))
btn_1.pack(side=tk.LEFT)
btn_2 = tk.Button(frame_btns_5, text=".", command=lambda: btn_click("."))
btn_2.pack(side=tk.LEFT)
btn_3 = tk.Button(frame_btns_5, text="=", command=bt_equal)
btn_3.pack(side=tk.RIGHT)

window.mainloop()
