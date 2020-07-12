import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import pyperclip

root = tk.Tk()
root.title('Usecret')
root.iconbitmap('Image\shield.ico')
root.geometry('750x500+350+100')
root.resizable(False, False)
root.configure(bg='#404040')
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

#####################################################################
####################### Data Handling Section #######################
hint_data = tk.StringVar()
password_len = tk.IntVar()
final_password = tk.StringVar()
password_hint = tk.StringVar()


def generate_password():
    password = ''
    pass_selector = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                     'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                     '!', '@', '#', '$', '%', '&', '*']

    try:
        if password_len.get() > 20:
            hint_data.set('>Password Can not be greater than 20 !')
            help_label.config(fg='red')
        else:
            if password_len.get() == 0:
                hint_data.set('Password Length Can Not Be 0 !')
                help_label.config(fg='red')
            else:
                for n in range(password_len.get()):
                    password = password + random.choice(pass_selector)
                    password_entry_box.delete(0, 'end')
                    password_entry_box.insert(0, password)
                    final_password.set(password)
                hint_data.set(f'> Good Job !\n'
                              f'> Your Password is {password}\n'
                              f'> Press Copy To Clipboard button !')
                help_label.config(fg='green')
                help_label.config(justify='left')

    except:
        hint_data.set('> Please Enter Any Number !')
        help_label.config(fg='red')


def delete_password_length_field():
    password_length_entry_box.delete(0, 'end')
    password_entry_box.delete(0, 'end')
    password_entry_box.insert(0, 'Your Password Will Appear Here !')
    hint_data.set('')


def copy_in_clipboard():
    try:
        if password_len.get() == 0:
            hint_data.set('>First Generate Your Password !')
            help_label.config(fg='red')

    except:
        hint_data.set('>First Generate Your Password !')
        help_label.config(fg='red')
    pyperclip.copy(final_password.get())


def show_help():
    hint_data.set('> Enter Password Length : Max 20 Character !\n'
                  '> Click Generate Password Button!\n'
                  '> Click Copy To Clipboard Button!\n'
                  '> Click Reset Button To Clear Filed !\n'
                  '> Try It Now !!!')


def clear_length_entry_filed(event):
    password_length_entry_box.delete(0, 'end')


######################### Data Handling Section End ##################


#####################################################################
row_one_frame = tk.Frame(root)
row_one_frame.grid(row=0, column=0, sticky='ew')
row_one_frame.columnconfigure(1, weight=1)

avtar_icon = Image.open('Image\shield.png').resize((100, 100))
final_avtar = ImageTk.PhotoImage(avtar_icon)

avtar = tk.Label(row_one_frame, text='Profile',
                 height=100,
                 width=100,
                 image=final_avtar)
avtar.photo = final_avtar
avtar.config(bg='orange')
avtar.grid(row=0, column=0, sticky='ewns')

heading = tk.Label(row_one_frame, text='Password Generator',
                   font='roboto 35 bold',
                   bg='orange')
heading.grid(row=0, column=1, sticky='ewns')

help_icon = Image.open('Image\icons8-question-mark-96.png').resize((100, 100))
final_help_icon = ImageTk.PhotoImage(help_icon)

help_button = tk.Button(row_one_frame, text='Help',
                        cursor='hand2',
                        image=final_help_icon,
                        height=100,
                        bg='red',
                        bd=5,
                        command=show_help,
                        width=100)
help_button.photo = final_help_icon
help_button.grid(row=0, column=2, sticky='ewns')

######################################################################
row_two_frame = tk.Frame(root, bg='#404040')
row_two_frame.grid(row=1, column=0, sticky='ew')
row_two_frame.columnconfigure(2, weight=1)

password_length_label = tk.Label(row_two_frame,
                                 text='Password Length',
                                 anchor='w',
                                 width=15,
                                 font='times 15 bold')
password_length_label.grid(row=0, sticky='nsew', column=0, pady=3)

password_label = tk.Label(row_two_frame,
                          text='Pasword',
                          anchor='w',
                          width=15,
                          font='times 15 bold')
password_label.grid(row=1, sticky='nsew', column=0)

password_length_entry_box = tk.Entry(row_two_frame,
                                     font='times 15 bold',
                                     textvariable=password_len,
                                     width=35)
password_length_entry_box.grid(row=0, column=1, sticky='nsew', padx=3, pady=3)
password_length_entry_box.bind('<Button-1>', clear_length_entry_filed)

password_entry_box = tk.Entry(row_two_frame,
                              font='times 15 bold',
                              textvariable=password_hint,
                              width=35)
password_entry_box.grid(row=1, column=1, sticky='nsew', padx=3)
password_hint.set('Your Password Will Appear Here !')

reset_button = tk.Button(row_two_frame,
                         text='Reste',
                         bg='red',
                         bd=5,
                         cursor='hand2',
                         command=delete_password_length_field,
                         font='times 15 bold')
reset_button.grid(row=2, column=0, sticky='nsew', pady=3)

copy_to_clipboard_button = tk.Button(row_two_frame,
                                     text='Copy To Clipboard',
                                     cursor='hand2',
                                     bd=5,
                                     bg='#ff9900',
                                     command=copy_in_clipboard,
                                     font='times 15 bold')
copy_to_clipboard_button.grid(row=2, column=1, columnspan=1, sticky='nsew', pady=3)

password_generate_button = tk.Button(row_two_frame,
                                     text='Generate Password',
                                     bd=5,
                                     bg='#00802b',
                                     cursor='hand2',
                                     command=generate_password,
                                     font='times 15 bold')
password_generate_button.grid(row=0, column=2, rowspan=4, sticky='nsew', pady=(0, 3))

help_label = tk.Label(root, text='> Hint',
                      fg='red',
                      font='times 20',
                      textvariable=hint_data,
                      anchor='nw',
                      justify='left',
                      bg='#404040')
help_label.grid(row=2, column=0, sticky='nsew')
root.mainloop()
