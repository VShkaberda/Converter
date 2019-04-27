# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:44:55 2019

@author: Vadim Shkaberda
"""

import re
import tkinter as tk


def paste():
    ''' Paste data from cliboard at the end of Entry.
    '''
    ent.insert( "insert", root.clipboard_get() )


def select_all():
    ''' Select all data in Entry box.
    '''
    ent.tag_add(tk.SEL, "1.0", tk.END)
    ent.mark_set(tk.INSERT, "1.0")
    ent.see(tk.INSERT)


def tr():
    ''' Transpose rows into columns.
    '''
    s = ent.get("1.0", tk.END)
    if as_txt.get():  # check if want int or text as output
        s = re.sub(r"(\w+)", r"'\1'", s)
    s = s.strip().replace('\n', ', ')
    clear()
    ent.insert("insert", s)
    # select text
    select_all()


def copy():
    ''' Copy data to the clipboard and let it stay there after the window is closed.
    '''
    root.clipboard_clear()
    root.clipboard_append(ent.get("1.0", tk.END))
    root.update()


def clear():
    ''' Clear text box.
    '''
    ent.delete("1.0", tk.END)


root = tk.Tk()
root.title('Конвертер')    # window name
root.geometry('500x400')

top = tk.Frame(root)
bottom = tk.Frame(root)
top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
bottom.pack(side=tk.BOTTOM, expand=False)

ent = tk.Text(top, width=50, height=20)    # input and output box
ent.pack(in_=top)
ent.focus()  # no need to click to focus

as_txt = tk.IntVar()
c = tk.Checkbutton(top, text="Транспонировать как текст", variable=as_txt)
c.pack(in_=top, side=tk.BOTTOM)

buttons = (("Вставить", "paste"), ("Перевести", "tr"), ("Копировать", "copy"), ("Очистить", "clear"), ("Выход", "root.destroy"))

for but, comm in buttons:
    exec('tk.Button(bottom, text="{0}", width=10, height=2, command={1}).pack(in_=bottom, side=tk.LEFT)'.format(but, comm))

root.mainloop()