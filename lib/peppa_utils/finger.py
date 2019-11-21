# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 11:08 AM
# @Author  : nJcx
# @Email   : njcx86@gmail.com
# @File    : finger.py

from Wappalyzer.Wappalyzer import Wappalyzer, WebPage


class FinerPrint(object):
    def __init__(self):



wappalyzer = Wappalyzer()
webpage = WebPage.new_from_url('https://www.runoob.com/')
wappalyzer.analyze_with_categories(webpage)
wappalyzer.analyze_with_categories(webpage)
