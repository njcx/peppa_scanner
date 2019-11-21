# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com
# @File    : peppa-scanner.py
import sys
import os
import argparse
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + "lib"))
from pyfiglet import Figlet
from Wappalyzer.Wappalyzer import Wappalyzer, WebPage


def banner():
    banner_ = Figlet(font='slant')
    print(banner_.renderText('Peppa-Scanner'))
    print("<---------WELCOME TO USE THIS PROGRAM--------->")
    print("<---------v1.0 - Author - nJcx86--------->")
    print("\n")


def parse_options():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, add_help=False)

    parser.add_argument("-h", "--help", action="help",
                        help="Show help message and exit")

    target = parser.add_argument_group('[ Targets ]')

    target.add_argument("-u", "--url", dest="url",
                        help="Target URL (e.g. \"https://www.google.com/\")")

    target.add_argument("-t", "--threads", dest="process_num",
                        help="max number of process, default cpu number")

    request = parser.add_argument_group('[ Request Option ]')

    request.add_argument("--cookie", dest="cookie",
                         help="HTTP Cookie header value")

    request.add_argument("--referer", dest="referer",
                         help="HTTP Referer header value")

    request.add_argument("--user-agent", dest="agent",
                         help="HTTP User-Agent header value")

    request.add_argument("--random-agent", dest="randomAgent", action="store_true", default=False,
                         help="Use randomly selected HTTP User-Agent header value")

    request.add_argument("--timeout", dest="timeout",
                         help="Seconds to wait before timeout connection (default 30)")

    request.add_argument("--retry", dest="retry", default=False,
                         help="Time out retrials times.")

    args = parser.parse_args()

    return args.__dict__


if __name__ == "__main__":

    banner()
    parse_options()
    wappalyzer = Wappalyzer()
    webpage = WebPage.new_from_url('https://www.runoob.com/')
    print(wappalyzer.analyze_with_categories(webpage))


