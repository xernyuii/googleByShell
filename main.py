#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import sys,os
import webbrowser
import json
import urllib
import urllib2
import os.path

"""
googleByShell - Simple tool search in google/baidu/wikipedia/etc by shell
@Auther XeRn(hfutxc.xern@gmail.com)
@Date   2017.1.14
"""

class Search:
    def __init__(self, argv):
        self.check(argv)
    def check(self, argv):

        if argv[1].startswith("--"):
            option = argv[1][2:]

            if option == 'version' or option =='v':
                print('googleByShell version 1.1.0')

            elif option == 'help' or option == 'h':
                print('gooleByShell usage list: ')
                print('usage: google/baidu/wiki/translate [--h] [--v] [%s] [--d] [--nd]')
                print('')
                print('google:            Search sth by google(may need vpn)')
                print('baidu:             Search sth by baidu')
                print('wiki:              Search sth by wikipedia(may need vpn)')
                print('translate, tsl     Translate words or sentences by youdao')
                print('')
                print('optional arguments:')
                print('--h, --help        Show help message and exit')
                print('--v, --version     Show version and exit')
                print('--d                Turn on debug mode')
                print('--nd               Turn off debug mode')

        elif 'translate' in argv[0]:
            self.translate(argv[1:])
        else:
            self.search(argv)

    def search(self, argv):
        urls = {
            'google': 'https://www.google.com.hk/search?q=',
            'baidu': 'https://www.baidu.com/s?wd=',
            'wiki': 'https://en.wikipedia.org/wiki/',
        }
        extra_args = {
            'google': '&ie=utf-8&oe=utf-8',
            'baidu': '&ie=utf-8&oe=utf-8',
            'wiki': ''
        }
        url = urls[os.path.basename(argv[0])]
        for item in argv[1:]:
            url += item+' ';
        url+=extra_args[os.path.basename(argv[0])]
        webbrowser.open_new_tab(url)

    def translate(self,argv):
        keyfrom = 'googleByShell'
        key = '616691616'
        api = 'http://fanyi.youdao.com/openapi.do?keyfrom=googleByShell&key='+key+'&type=data&doctype=json&version=1.1&q='
        url = api
        for item in argv:
            url += ' '+item
        data = json.loads(urllib2.urlopen(url).read())
        errorCodes = {
            0: 'success',
            20: "WARNING: Word too long",
            30: "WARNING: Translate Error",
            40: "WARNING: Do not support this language",
            50: "WARNING: Key failed",
            60: "WARNING: Do not have this word"
        }
        code = data['errorCode']

        if code == 0:
            try:
                u = data['basic']['us-phonetic']
                e = data['basic']['uk-phonetic']
                c = data['basic']['phonetic']
            except KeyError:
                c = 'None'
                u = 'None'
                e = 'None'

            try:
                explains = data['basic']['explains']
            except KeyError:
                explains = 'None'

            print(data['query'])
            #print(data['translation'])

            if explains != 'None':
                for item in explains:
                    print(item)
            else:
                print("No explain")

        else:
            print(errorCodes[code])

if __name__ == '__main__':
    Search(sys.argv)

