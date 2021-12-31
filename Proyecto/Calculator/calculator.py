import tkinter as ttk

window = ttk.Tk()

window.title("Calculator")
window.geometry("500x400")


def clear_display():
    display_text.set("")

def button_click(button_content):
    current_value = display_text.get()
    next_value = current_value + button_content

    display_text.set(next_value)


def solve():
    current_value = display_text.get()
    result = str(eval(current_value))

    display_text.set(result)


display_text = ttk.StringVar()


display_frame = ttk.Frame(window, width=312, height=50)
display_frame.pack(side=ttk.TOP)

input_field = ttk.Entry(display_frame, width=55,
                        textvariable=display_text, bg="#eee", justify=ttk.RIGHT)

input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

buttons_frame = ttk.Frame(window, width=312, height=310, bg="#eee")
buttons_frame.pack()

clear = ttk.Button(buttons_frame, text="C", bg="#deaa87", width=38,
                   height=3, fg="#4d4d4d", cursor="hand2", command=clear_display)
clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = ttk.Button(buttons_frame, text="/", bg="white",
                    width=10, height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("/"))
divide.grid(row=0, column=3, padx=1, pady=1)


seven = ttk.Button(buttons_frame, text="7", bg="#deaa87",
                   width=10, height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("7"))
seven.grid(row=1, column=0, padx=1, pady=1)

eight = ttk.Button(buttons_frame, text="8", bg="#deaa87",
                   width=10, height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("8"))
eight.grid(row=1, column=1, padx=1, pady=1)

nine = ttk.Button(buttons_frame, text="9", bg="#deaa87",
                  width=10, height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("9"))
nine.grid(row=1, column=2, padx=1, pady=1)

multiply = ttk.Button(buttons_frame, text="*", bg="white",
                      width=10, height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("*"))
multiply.grid(row=1, column=3, padx=1, pady=1)


four = ttk.Button(buttons_frame, text="4", bg="#deaa87",
                  width=10, height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("4"))
four.grid(row=2, column=0, padx=1, pady=1)

five = ttk.Button(buttons_frame, text="5", bg="#deaa87",
                  width=10, height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("5"))
five.grid(row=2, column=1, padx=1, pady=1)

six = ttk.Button(buttons_frame, text="6", bg="#deaa87",
                 width=10, height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("6"))
six.grid(row=2, column=2, padx=1, pady=1)

minus = ttk.Button(buttons_frame, text="-", bg="white",
                   width=10, height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("-"))
minus.grid(row=2, column=3, padx=1, pady=1)


one = ttk.Button(buttons_frame, text="1", bg="#deaa87",
                 width=10, height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("1"))
one.grid(row=3, column=0, padx=1, pady=1)

two = ttk.Button(buttons_frame, text="2", bg="#deaa87",
                 width=10, height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("2"))
two.grid(row=3, column=1, padx=1, pady=1)

three = ttk.Button(buttons_frame, text="3", bg="#deaa87",
                   width=10, height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("3"))
three.grid(row=3, column=2, padx=1, pady=1)

plus = ttk.Button(buttons_frame, text="+", bg="white",
                  width=10, height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("+"))
plus.grid(row=3, column=3, padx=1, pady=1)


zero = ttk.Button(buttons_frame, text="0", bg="#deaa87",
                  width=24, height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("0"))
zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

dot = ttk.Button(buttons_frame, text=".", bg="white", width=10,
                 height=3, fg="#4d4d4d", cursor="hand2", command=lambda: button_click("."))
dot.grid(row=4, column=2, padx=1, pady=1)

equal = ttk.Button(buttons_frame, text="=", bg="white",
                   width=10, height=3, fg="#4d4d4d", cursor="hand2", command=solve)
equal.grid(row=4, column=3, padx=1, pady=1)


window.mainloop()
