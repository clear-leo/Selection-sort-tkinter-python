#YAYYY tkinter time!!
import tkinter as tk
import ttkbootstrap as ttk #do not forget to install this

#Good luck!
arr = []

def add_list(): 
    entry1_var.set(entry1.get())

    arr.append(int(entry1_var.get()))
    arr_label_var.set(arr)

def rmv_list():
    arr.pop(-1)
    arr_label_var.set(arr)    

def sort_list():
    size = len(arr)    

    for ind in range(size):
        vind = ind
        for i in range(vind + 1, size):
            if arr[ind] > arr[i]:
                vind = i
            else: 
                i =+ 1
        (arr[ind], arr[vind]) = (arr[vind], arr[ind])
    arr_label_var.set(arr)    
    


window = tk.Tk()
window.geometry("400x300")

title_frame = tk.Frame(window)
title_frame.pack(pady = 20)

title_text1 = tk.Label(title_frame, text='Selection sort', font="Arial 24 bold")
title_text1.pack(side='left')

title_text2 = tk.Label(title_frame, text='ish', font='Arial 10')
title_text2.pack(side='bottom')

entry1 = ttk.Entry(window, font = "Calibri 10", )
entry1_var = tk.StringVar()
entry1.pack()

intr_frame = tk.Frame(window)
intr_frame.pack(pady=10)
#Had to redesign from this part downward entirely
#don't mind the names I'm working on it

append_button = ttk.Button(intr_frame, text = 'Add', command=add_list)
append_button.pack(side='left', padx = 10)

clear_button = ttk.Button(intr_frame, text = 'Clear', command=rmv_list)
clear_button.pack(side='right', padx = 10)

sort_button = ttk.Button(window, text = 'Sort!', command=sort_list)
sort_button.pack()

arr_label_var = tk.StringVar()
arr_label = tk.Label(window, textvariable=arr_label_var, font='Arial 18 bold')
arr_label.pack()

window.mainloop()

#blep