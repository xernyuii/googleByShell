#!/usr/bin/env python

import sys,os 
import webbrowser

"""

googleByShell - Simple tool search in google/baidu/wikipedia/etc by shell
@Auther XeRn(hfutxc.xern@gmail.com)
@Date   2017.1.14
"""


class Search:


    def __init__(self, argv):
        self.check(argv)
    
    def check(self, argc):

        if argc[1].startswith("--"):
            option = argc[1][2:]

            if option == 'version' or option =='v':
                print 'googleByShell version 1.0.1 test '
            
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

        elif 'google' in argc[0]:
            
            self.google(argc[1:])

        elif 'baidu' in argc[0]:
            self.baidu(argc[1:])

        elif 'wiki' in argc[0]:
            self.wiki(argc[1:])

    def google(self,argc):
        
        url = 'https://www.google.com.hk/search?q='

        for item in argc:
            url += ' '
            url += item
        
        webbrowser.open_new_tab(url)
    
    def baidu(self,argc):

        url = 'https://www.baidu.com/s?wd='
        for item in argc:
            url += ' '
            url += item

        webbrowser.open_new_tab(url)

    def wiki(self,argc):

        url = 'https://en.wikipedia.org/wiki/'
        for item in argc:
            url += ' '
            url += item

        webbrowser.open_new_tab(url)


    
if __name__ == '__main__':
    Search(sys.argv)













