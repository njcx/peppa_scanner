# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 4:43 PM
# @Author  : nJcx
# @Email   : njcx86@gmail.com
# @File    : color_print.py

from colorama import init, Fore


class ColorPrint(object):

    def __init__(self):
        init(autoreset=True)

    def red(self, message):
        print(Fore.RED + str(message))

    def green(self, message):
        print(Fore.GREEN + str(message))

    def yellow(self, message):
        print(Fore.YELLOW + str(message))

    def white(self, message):
        print(Fore.WHITE + str(message))

    def blue(self, message):
        print(Fore.BLUE + str(message))

    def cyan(self, message):
        print(Fore.CYAN + str(message))

    def magenta(self, message):
        print(Fore.MAGENTA + str(message))





