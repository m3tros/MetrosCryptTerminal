 

<p align="center"> 
  <img src="https://user-images.githubusercontent.com/107058068/172821950-664bb083-8a47-4a26-b43d-e61551716b01.png" alt="MetrosCryptTerminal" width="80px" height="80px">
</p>
<h1 align="center">MetrosCryptTerminal</h1>

## Description
MetrosCryptTerminal is for file encryption/decryption based on the <a href="https://pypi.org/project/cryptocode/">cryptocode</a> algorithm.<br>
It is written in <a href="https://python.org">Python</a> <a href="https://www.python.org/downloads/release/python-3104/">3.10.4</a> 
The program is distributed in forms as an open source python file and an executable file for Linux and Windows.<br>


<p align="center"> 
  <img src="https://user-images.githubusercontent.com/107058068/173620583-08fcf652-26f1-4905-b2bf-1110d303b883.png" alt="MetrosCryptTerminal">
</p>
In executable files, the program is exclusively in English with   without the possibility of changing settings.<br>

- To output the help of a specific command, type `help` and `command`.

## Other versions of the program
- <a href="https://github.com/John-MetrosSoftware/MetrosCrypt">MetrosCrypt</a>
- <a href="https://github.com/John-MetrosSoftware/MetrosCryptTerminal">MetrosCryptTerminal</a> (Current)
- <a href="https://github.com/John-MetrosSoftware/MetrosCryptTerminalGUI">MetrosCryptTerminalGUI</a> 

## Installation for python3
### Libraries
- <a href="https://pypi.org/project/pyfiglet/0.7/">pyfiglet</a>
- <a href="https://pypi.org/project/cryptocode/">cryptocode</a>
- <a href="https://pypi.org/project/colorama/">colorama</a>
- <a href="https://pypi.org/project/prompt-toolkit/0.5/">prompt_toolkit</a>

```
git clone https://github.com/John-MetrosSoftware/MetrosCryptTerminal
cd MetrosCryptTerminal
pip3 install -r requirements.txt
python3 MetrosCryptTerminal.py
```
## Usage
### help
```
Usage:  [command] <options>

        cd                      Change the directory
        clean, clear, cls       Clear terminal screen
        decrypt <filename>      Decrypt file
        echo <text>             Text output to screen
        encrypt <filename>      Encrypt file
        exit, quit              Exit program
        help <command>          Output help about commands
        ls <directory>          Output contents of folder
        print                   Output of file contents
        print_decrypt           Decrypt contents of file and output
        print_encrypt           Encrypt contents of file and output
        pwd                     Output current directory
        system <command>        Execute system terminal command
```
### cd
```
Usage:  cd              Output current directory
        cd ..           Go back
        cd <directory>  Go to a specific directory

The cd 'change directory' command is used to change the current working directory.
```
### clean, clear, cls
```
Usage:  clean   Clear terminal screen

Just clears the program's terminal screen.
```
### decrypt
```
Usage:  decrypt <file>  Decrypt file

Decrypts the file by password.

After the transfer of a specific file, it is checked whether it exists, if not, an error is displayed:
        * Could not find the file.

And if it exists, the program asks for a password, if the password is incorrect, an error is displayed:
        * Passwords don't match...

Further, if everything is correct, the result of the decrypted will be written to the input file, if this does not work, an error is output:
        * An error occurred when writing the result to a file.

If everything is correct, the message is displayed:
        * Completed successfully! The file was decrypted.

[*] Encryption or decryption algorithm: https://pypi.org/project/cryptocode/
```
### echo
```
Usage:  echo <text>     Text output to screen

Echo command is used to display line of text/string that are passed as an argument.

[*] To enable or disable command output mode on the screen, use the following parameters: 'on' or 'off'.
```
### encrypt
```
Usage:  encrypt <file>  Encrypt file

Encrypts the file by password.

After the transfer of a specific file, it is checked whether it exists, if not, an error is displayed:
        * Could not find the file.

For security, the program uses password guessing, if they do not match, then an error is displayed:
        * Passwords don't match...

And if it exists, the program asks for a password, if the password is incorrect, an error is displayed:
        * Password is incorrect...

Further, if everything is correct, the result of the encrypted will be written to the input file, if this does not work, an error is output:
        * An error occurred when writing the result to a file.

If everything is correct, the message is displayed:
        * Completed successfully! The file was encrypted.

[*] Encryption or decryption algorithm: https://pypi.org/project/cryptocode/
```
### exit, quit
```
Usage:  exit    Exit program

Completion of the program.
```
### ls
```
Usage:  ls              Display folders and files in the current directory
        ls <directory>  Display folders and files in a specific directory

The ls command outputs a list of files and directories within the directory.
```
### print
```
Usage:  print <file>    Output of file contents

Display the contents of a specific file.
```
### print_decrypt
```
Usage:  print_decrypt   Decrypt contents of file and output

Decryption of the contents of the file and the output of the result.

First, the existence of the file is checked, if it does not exist, an error is displayed:
        * Could not find file.
Then you need to enter a password in order to be able to decrypt the contents of the file; if the password is incorrect, an error is displayed:
        * Password is incorrect...
After which the decrypted text is displayed on the screen and below the file name.

Getting the contents of the file ➜ Decryption by password ➜ Displaying the result.

[*] Encryption or decryption algorithm: https://pypi.org/project/cryptocode/
```
### print_encrypt
```
Usage:  print_encrypt    Encrypt contents of file and output

Encryption of the contents of the file and the output of the result.

First, the existence of the file is checked, if it does not exist, an error is displayed:
        * Could not find file.
Then you need to enter a password in order to be able to encrypt the contents of the file; if the password is incorrect, an error is displayed:
        * Password is incorrect...
After which the encrypted text is displayed on the screen and below the file name.

Getting the contents of the file ➜ Encryption by password ➜ Displaying the result.

[*] Encryption or decryption algorithm: https://pypi.org/project/cryptocode/
```
### pwd
```
Usage:  pwd     Output current directory

The pwd command prints the current working directory path.
```
### system
```
Usage:  system          (Input) Execute system terminal command
        system <command>        Execute system terminal command

Execution of terminal commands. To work from the MetrosCrypt terminal.
```
## Possible mistakes
### help
```
There is no help for such a command: <command>
```
The error lies in the fact that the program does not have help for the command you enter.
### encrypt
Missing parameters.
```
To execute the '<command>' command, a parameter is required '<parameter>'.
```
The error lies in the fact that for encryption it is necessary to confirm the password, this is done for security, if they do not match, then an error is displayed.
```
Passwords don't match...
```
The error lies in the fact that the file cannot be encrypted. Concretely, the encryption function returns `false`.
```
Apparently it was not possible to encrypt the file (<file>).
```
The error is that there was an error writing the result to the file.
```
An error occurred when writing the result to a file (<file>).
```
The error is that the file does not exist.
```
Could not find the file (<file>).
```
### decrypt
Missing parameters.
```
To execute the '<command>' command, a parameter is required '<parameter>'.
```
Incorrect password for decrypting the file.
```
Password is incorrect...
```
The error is that there was an error writing the result to the file.
```
An error occurred when writing the result to a file (<file>).
```
The error is that the file does not exist.
```
Could not find the file (<file>).
```
### print_encrypt
Missing parameters.
```
To execute the '<command>' command, a parameter is required '<parameter>'.
```
The error lies in the fact that the file cannot be encrypted. Concretely, the encryption function returns `false`.
```
Apparently it was not possible to encrypt the file (<file>).
```
The error is that the file does not exist.
```
Could not find the file (<file>).
```
### print_decrypt
Missing parameters.
```
To execute the '<command>' command, a parameter is required '<parameter>'.
```
Incorrect password for decrypting the file.
```
Password is incorrect...
```
The error is that the file does not exist.
```
Could not find the file (<file>).
```
### MetrosCrypt Terminal
Couldn't find command. Check the syntax for writing the command.
```
Unknown command: <command>
```
If this error occurs, then something has happened to the program's startup function.
```
Unknown error: <error>
```
## Messages
### help
In order to display detailed command help, you must use the `help` command and the name of the `command`.
```
To output the help of a specific command, type 'help' and 'command'.
```
### encrypt
The message means that everything was successful.
```
Completed successfully! The file (<file>) was encrypted.
```
### decrypt
The message means that everything was successful.
```
Completed successfully! The file (<file>) was decrypted.
```

## Compilation
This version 1.0 is a version without saving any settings or changing them.<br>
All software is provided in English with executable files, these parameters cannot be changed.<br>
I usually compile my projects using the <a href="https://pypi.org/project/pyinstaller/">pyinstaller</a> compiler with the following parameters:
This version 1.0 is a version without saving any settings or changing them.<br>
All software is provided in English with executable files, these parameters cannot be changed.<br>
I usually compile my projects using the <a href="https://pypi.org/project/pyinstaller/">pyinstaller</a> compiler with the following parameters:
```
pyinstaller -F MetrosCryptTerminal.py
```
Adding an icon for the executable file. You can use yours.
```
pyinstaller -F --icon=1.ico MetrosCryptTerminal.py
```
The icon '1.ico' can be downloaded from the <a href="https://download.flaticon.com/ru/download/icon/7721624?icon_id=7721624&author=3428&team=3428&keyword=%D0%97%D0%B0%D0%B1%D0%BB%D0%BE%D0%BA%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C+%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD&pack=7721572&style=Mixed&style_id=1285&format=png&color=%23000000&colored=2&size=512%2C256%2C128%2C64%2C32%2C24%2C16&selection=1&premium=&type=standard&token=03AGdBq27PWtVknlV1cRpjntK0Skz1AKUs7v05aWKzNZG9F9F1yHLUbVoqqHLhDfpK8xmzCy_x9G2NGGQQSrw0vEChiPOHlZmgZPetu8P7LXSfDhcC8z3JA3jzq1jBOmu6HY2-HXP0KnM0xxGUS5jHMiLMzbL2MkqQXPH-m4qb5HotPEgIVxndwWTEd9Cj-1J23E1mzETB-PDKitdhrT1poO-OUZMn6frg7_UeNLZZ2sejSqPLt7Da9jwr6RR7QX6_Is5EtM6kMfgGbXU2Zua2mZ8_todQdwNcm9scGi5CBQIpE4L93P1NfJBx18LhAzLutDC1lev_cHJ2RbgXUzZHX9kgvAD7v9j5kz5gfzBOGTEQtgcqwXxNWv2uL_O3Lg341o1TADm083QAFiJrJmoI1fCR8NrnHKyCJ6A795xI84u7pleo2Mm6FwhdFTUic9VUNzFt-dzvOvu_IuxAoE2D_V0dAlI2uS5jIfbAC1NvlL7Vndmc7SyxN_Zhx_0AE3sjvlcsYs2ougeWHcb7-G9nWyM1HXC5iHxp2nIT_ubAyOzDywS_MRYPq3vShzWtSKeJFuLcxNt9s1aWx-OMjRAj0HWu4LODOx3aotaLOXvpyQU0G1K_g2qpB6w3lSb-8V44LTZB5S1JUM3EivTDeMuMxATLXSOzWV6EJ3mNW5Auh3zdvJPMBX5qpXtmt1NeSGJN4K7gO-Ze5Cfuo7522pm_Mrlhbl2IwCnist4R8Y7mFSUIFSOUtEodfyj7X3PlhzIHWJ967QOilHLyxzoJxB3xZYWDIkVZshyNuorF6PjgaRmNLO7SL5ZmrRLirjhDEPPsY53LZjY-_yvg6BfdFstRv2dtYsZhZV5vwelpC8RkPMYITKRk4xdb7ivHMRb7_ZBpw68wmh8G3Sor0H7uT6INgbtjzJm0q4P9GT6RqXzF0ubFQojUofLfBA2jO355l5unIkwQgh-xoxamxGoSRdvVL_6qAJG7Bk9yuqkbimEmCRuplzgwbtLy_KsyTyi6nsWrGnhjASAv4UyA_AieVjmThe-e7g6ZXzuPXCLGjsVKEjb4XE_cQ2m5n14jxx4B8FgRydFbueUa4E7fLh1koHFJvB_YJK8_8r8BwuwSia2Q5CXHOmKJwUiMC6tvnyBIgFAW4TiMapmX2jMXO9A67kUr6M80V2P7hWietInTDOnAykx5vG032oz4o41UdehHbd6fuRVXrAAK1f10MNfrGn9jOyZG2ELmGCvxVcnhw-aAlgPLjr3ZGbcZVRGsYX0BTlc-XptVKZfIKN9b1UZVAlCa4ZctuNrXk2JEAhrKvFKQ6Oa_mb62Vt3cY2xOk_57QEHp9P-eNzh02Fv3OxfMUFtrvTQLp35G8VIzfWmDFTi4sGbBvbi9PUhF1RXwG7kGDda87u9a6RyWW6z8BPyi4KI2TOfbthI9A-A-IJgZi16Qms0tI1GmccP_aXw1FpZEAbvX46MlBhOmJsIu9hE89YOhwc3vhYmP0itR79A1oJw_EMK87KR1DM-JB4MMpt8y0kR71vhJgtqHeUFO&search=%D0%B7%D0%B0%D0%BC%D0%BE%D0%BA+%D0%B7%D0%B0%D0%BA%D1%80%D1%8B%D1%82%D1%8B%D0%B9">link</a>.<br>
When making edits in the code or other changes, mark the author I want to know how the project is developing.
## PEP8
<a href="https://pypi.org/project/autopep8/">autopep8</a> automatically formats Python code to conform to the PEP 8 style guide. It uses the pycodestyle utility to determine what parts of the code needs to be formatted. autopep8 is capable of fixing most of the formatting issues that can be reported by pycodestyle.
```
autopep8 MetrosCryptTerminal.py --recursive --in-place
```
## Developer 
Telegram : https://t.me/metrossoftware
