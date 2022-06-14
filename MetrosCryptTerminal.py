import os
import sys
import shlex
import pyfiglet
import cryptocode
import maskpass
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
from prompt_toolkit.history import FileHistory
from prompt_toolkit.cursor_shapes import CursorShape
from colorama import Fore


def message(text):
    print('{}[*]{} {}'.format(Fore.BLUE, Fore.WHITE, text))


def errors(text):
    print('{}[!]{} {}'.format(Fore.RED, Fore.WHITE, text))


def no_parameters(command, parameter):
    message(
        f'To execute the \'{command}\' command, a parameter is required \'{parameter}\'.')


class Main:

    def __init__(self):
        super().__init__()
        self.start_program = True
        self.session = PromptSession()  # history
        self.prompt_text = HTML(
            '\n<font color="#00bfff">[MetrosCrypt Terminal]</font> <b>{}</b><font color="#00bfff">$</font> '.format(os.getcwd()))
        self.temp_prompt = self.prompt_text
        while self.start_program == True:
            self.init()

    def init(self):
        try:
            self.command_input = self.session.prompt(
                self.prompt_text, auto_suggest=AutoSuggestFromHistory(), completer=command_list, cursor=CursorShape.BLINKING_BEAM)
            if self.command_input.replace(' ', '') != '':
                self.command_input_split = shlex.split(self.command_input)
                try:
                    self.command()
                except Exception as error:
                    errors(error)

        except KeyboardInterrupt:
            self.start_program = False
        except EOFError:
            pass

    def command(self):
        if str(self.command_input_split[0]).lower() == 'help':
            if str(self.command_input_split[-1]) == 'help':
                print('Usage:\t[command] <options>\n\n\tcd\t\t\tChange the directory\n\tclean, clear, cls\tClear terminal screen\n\tdecrypt <filename>\tDecrypt file\n\techo <text>\t\tText output to screen\n\tencrypt <filename>\tEncrypt file\n\texit, quit\t\tExit program\n\thelp <command>\t\tOutput help about commands\n\tls <directory>\t\tOutput contents of folder\n\tprint\t\t\tOutput of file contents\n\tprint_decrypt\t\tDecrypt contents of file and output\n\tprint_encrypt\t\tEncrypt contents of file and output\n\tpwd\t\t\tOutput current directory\n\tsystem <command>\tExecute system terminal command\n')
                message(
                    'To output the help of a specific command, type \'help\' and \'command\'.')
                return
            elif str(self.command_input_split[-1]).lower() == 'cd':
                print('''Usage:\tcd\t\tOutput current directory\n\tcd ..\t\tGo back\n\tcd <directory>\tGo to a specific directory\n\nThe cd \'change directory\' command is used to change the current working directory.''')
            elif str(self.command_input_split[-1]).lower() == 'cls' or str(self.command_input_split[-1]).lower() == 'clear' or str(self.command_input_split[-1]).lower() == 'clean':
                print(
                    f'Usage:\t{str(self.command_input_split[-1])}\tClear terminal screen\n\nJust clears the program\'s terminal screen.')
            elif str(self.command_input_split[-1]) == 'decrypt':
                print('Usage:\tdecrypt <file>\tDecrypt file\n\nDecrypts the file by password.\n\nAfter the transfer of a specific file, it is checked whether it exists, if not, an error is displayed:\n\t* Could not find the file.\n\nAnd if it exists, the program asks for a password, if the password is incorrect, an error is displayed:\n\t* Passwords don\'t match...\n\nFurther, if everything is correct, the result of the decrypted will be written to the input file, if this does not work, an error is output:\n\t* An error occurred when writing the result to a file.\n\nIf everything is correct, the message is displayed:\n\t* Completed successfully! The file was decrypted.\n')
                message(
                    'Encryption or decryption algorithm: https://pypi.org/project/cryptocode/')
            elif str(self.command_input_split[-1]) == 'encrypt':
                print('Usage:\tencrypt <file>\tEncrypt file\n\nEncrypts the file by password.\n\nAfter the transfer of a specific file, it is checked whether it exists, if not, an error is displayed:\n\t* Could not find the file.\n\nFor security, the program uses password guessing, if they do not match, then an error is displayed:\n\t* Passwords don\'t match...\n\nAnd if it exists, the program asks for a password, if the password is incorrect, an error is displayed:\n\t* Password is incorrect...\n\nFurther, if everything is correct, the result of the encrypted will be written to the input file, if this does not work, an error is output:\n\t* An error occurred when writing the result to a file.\n\nIf everything is correct, the message is displayed:\n\t* Completed successfully! The file was encrypted.\n')
                message(
                    'Encryption or decryption algorithm: https://pypi.org/project/cryptocode/')
            elif str(self.command_input_split[-1]) == 'exit' or str(self.command_input_split[-1]) == 'quit':
                print(
                    f'Usage:\t{str(self.command_input_split[-1])}\tExit program\n\nCompletion of the program.')
            elif str(self.command_input_split[-1]) == 'ls':
                print('Usage:\tls\t\tDisplay folders and files in the current directory\n\tls <directory>\tDisplay folders and files in a specific directory\n\nThe ls command outputs a list of files and directories within the directory.')
            elif str(self.command_input_split[-1]) == 'print_decrypt':
                print('Usage:\tprint_decrypt\tDecrypt contents of file and output\n\nDecryption of the contents of the file and the output of the result.\n\nFirst, the existence of the file is checked, if it does not exist, an error is displayed:\n\t* Could not find file.\nThen you need to enter a password in order to be able to decrypt the contents of the file; if the password is incorrect, an error is displayed:\n\t* Password is incorrect...\nAfter which the decrypted text is displayed on the screen and below the file name.\n\nGetting the contents of the file ➜ Decryption by password ➜ Displaying the result.\n')
                message(
                    'Encryption or decryption algorithm: https://pypi.org/project/cryptocode/')
            elif str(self.command_input_split[-1]) == 'print_encrypt':
                print('Usage:\tprint_encrypt\t Encrypt contents of file and output\n\nEncryption of the contents of the file and the output of the result.\n\nFirst, the existence of the file is checked, if it does not exist, an error is displayed:\n\t* Could not find file.\nThen you need to enter a password in order to be able to encrypt the contents of the file; if the password is incorrect, an error is displayed:\n\t* Password is incorrect...\nAfter which the encrypted text is displayed on the screen and below the file name.\n\nGetting the contents of the file ➜ Encryption by password ➜ Displaying the result.\n')
                message(
                    'Encryption or decryption algorithm: https://pypi.org/project/cryptocode/')
            elif str(self.command_input_split[-1]) == 'print':
                print(
                    'Usage:\tprint <file>\tOutput of file contents\n\nDisplay the contents of a specific file.')
            elif str(self.command_input_split[-1]) == 'pwd':
                print(
                    'Usage:\tpwd\tOutput current directory\n\nThe pwd command prints the current working directory path.')
            elif str(self.command_input_split[1]) == 'echo' and str(self.command_input_split[-1]) == 'on':
                print('Usage:\techo on\t\tEnable command output mode on the screen.')
            elif str(self.command_input_split[1]) == 'echo' and str(self.command_input_split[-1]) == 'off':
                print('Usage:\techo on\t\tDisable command output mode on the screen.')
            elif str(self.command_input_split[-1]) == 'echo':
                print('Usage:\techo <text>\tText output to screen\n\nEcho command is used to display line of text/string that are passed as an argument.\n')
                message(
                    'To enable or disable command output mode on the screen, use the following parameters: \'on\' or \'off\'.')
            elif str(self.command_input_split[-1]) == 'system':
                print('Usage:\tsystem\t\t(Input) Execute system terminal command\n\tsystem <command>\tExecute system terminal command\n\nExecution of terminal commands. To work from the MetrosCrypt terminal.')
            else:
                help_command = self.command_input_split
                del help_command[0]
                help_command = ' '.join(str(x) for x in help_command)
                print('There is no help for such a command: '+help_command)
                return
        elif str(self.command_input_split[0]).lower() == 'exit' or str(self.command_input_split[0]).lower() == 'quit':
            self.start_program = False
        elif str(self.command_input_split[0]).lower() == 'cls' or str(self.command_input_split[0]).lower() == 'clear' or str(self.command_input_split[0]).lower() == 'clean':
            os.system('clear')
        elif str(self.command_input_split[0]).lower() == 'encrypt':
            if str(self.command_input_split[-1]) == 'encrypt':
                no_parameters('encrypt', 'file')
                return
            if os.path.isfile(str(self.command_input_split[-1])) == True:
                file_name = str(self.command_input_split[-1])
                message('Enter the password after entering the file: ({}). will be encrypted.'.format(
                    file_name))
                password = maskpass.advpass(prompt='Password:', mask='*')
                password_confirm = maskpass.advpass(
                    prompt='Confirm password:', mask='*')
                if password != password_confirm:
                    errors('Passwords don\'t match...')
                    return
                result_file = cryptocode.encrypt(
                    open(file_name, encoding='utf-8', errors='ignore').read(), password)
                if result_file == False:
                    errors(
                        'Apparently it was not possible to encrypt the file ().'.format(file_name))
                    return
                try:
                    write_file = open(file_name, 'w+')
                    write_file.write(result_file)
                    write_file.close()
                except Exception as error:
                    errors(
                        'An error occurred when writing the result to a file ().'.format(file_name))
                    return
                else:
                    message(
                        'Completed successfully! The file ({}) was encrypted.'.format(file_name))
            else:
                errors('Could not find the file ({}).'.format(
                    str(self.command_input_split[-1])))
        elif str(self.command_input_split[0]).lower() == 'decrypt':
            if str(self.command_input_split[-1]) == 'decrypt':
                no_parameters('decrypt', 'file')
                return
            if os.path.isfile(str(self.command_input_split[-1])) == True:
                file_name = str(self.command_input_split[-1])
                message('Enter the password after entering the file: ({}). will be decrypted.'.format(
                    file_name))
                password = maskpass.advpass(prompt='Password:', mask='*')
                result_file = cryptocode.decrypt(
                    open(file_name, encoding='utf-8', errors='ignore').read(), password)
                if result_file == False:
                    errors('Password is incorrect...')
                    return
                try:
                    write_file = open(file_name, 'w+')
                    write_file.write(result_file)
                    write_file.close()
                except Exception as error:
                    errors(
                        'An error occurred when writing the result to a file ({}).'.format(file_name))
                    return
                else:
                    message(
                        'Completed successfully! The file ({}) was decrypted.'.format(file_name))
        elif str(self.command_input_split[0]).lower() == 'system':
            if str(self.command_input_split[-1]) == 'system':
                command = os.system(input('System:'))
                return
            os.system(str(self.command_input).replace('system', ''))
            return
        elif str(self.command_input_split[0]).lower() == 'ls':
            path = os.getcwd()
            if str(self.command_input_split[-1]) != 'ls':
                path = str(self.command_input_split[-1])
            for folder in os.listdir(path):
                if os.path.isdir(folder):
                    print(Fore.BLUE+folder+Fore.WHITE)
            for file in os.listdir(path):
                if os.path.isfile(file):
                    print(file)
        elif str(self.command_input_split[0]).lower() == 'cd':
            if str(self.command_input_split[-1]) == 'cd':
                print(os.getcwd())
                return
            os.chdir(str(self.command_input_split[-1]))
        elif str(self.command_input_split[0]).lower() == 'pwd':
            print(os.getcwd())
        elif str(self.command_input_split[0]).lower() == 'echo' and str(self.command_input_split[1]).lower() == 'on':
            self.prompt_text = self.temp_prompt
        elif str(self.command_input_split[0]).lower() == 'echo' and str(self.command_input_split[1]).lower() == 'off':
            self.prompt_text = ''
        elif str(self.command_input_split[0]).lower() == 'echo':
            if str(self.command_input_split[-1]) == 'echo':
                print()
            else:
                print(str(self.command_input_split[-1]))
        elif str(self.command_input_split[0]).lower() == 'print_encrypt':
            if str(self.command_input_split[-1]) == 'print_encrypt':
                no_parameters('print_encrypt', 'file')
                return
            if os.path.isfile(str(self.command_input_split[-1])) == True:
                file_name = str(self.command_input_split[-1])
                message('Enter the password after entering the file: ({}).\nIt will be encrypted and the result will be displayed on the screen.'.format(file_name))
                password = maskpass.advpass(prompt='Password:', mask='*')
                result_file = cryptocode.encrypt(
                    open(file_name, encoding='utf-8', errors='ignore').read(), password)
                if result_file == False:
                    errors('Password is incorrect...')
                    return
                print(result_file+'\n'+'_'*50 +
                      '\nEncrypt file: {}'.format(file_name))
            else:
                errors('Could not find the file ({}).'.format(
                    str(self.command_input_split[-1])))
        elif str(self.command_input_split[0]).lower() == 'print_decrypt':
            if str(self.command_input_split[-1]) == 'print_decrypt':
                no_parameters('print_decrypt', 'file')
                return
            if os.path.isfile(str(self.command_input_split[-1])) == True:
                file_name = str(self.command_input_split[-1])
                message('Enter the password after entering the file: ({}).\nIt will be decrypted and the result will be displayed on the screen.'.format(file_name))
                password = maskpass.advpass(prompt='Password:', mask='*')
                result_file = cryptocode.decrypt(
                    open(file_name, encoding='utf-8', errors='ignore').read(), password)
                if result_file == False:
                    errors('Password is incorrect...')
                    return
                print(result_file+'\n'+'_'*50 +
                      '\nDecrypt file: {}'.format(file_name))
            else:
                errors('Could not find the file ({}).'.format(
                    str(self.command_input_split[-1])))
        elif str(self.command_input_split[0]).lower() == 'print':
            if str(self.command_input_split[-1]) == 'print':
                no_parameters('print', 'file')
                return
            print(open(str(self.command_input_split[-1]), encoding='utf-8', errors='ignore').read(
            )+'\n'+'_'*50+'\nFile: {}'.format(str(self.command_input_split[-1])))
        else:
            print('Unknown command: '+self.command_input)
            return


def boot():
    os.system('clear')
    print(Fore.BLUE+pyfiglet.figlet_format('MetrosCrypt')+Fore.WHITE)
    message('MetrosCrypt Terminal [version 1.0] 2022.')
    message('Github: https://github.com/John-MetrosSoftware/MetrosCryptTerminal')
    Main()
    print('')
    message('Completing MetrosCrypt Terminal...')


if __name__ == '__main__':
    boot()
