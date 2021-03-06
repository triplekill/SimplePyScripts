#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'
 
 
"""Скрипт отправляет win7 в режим гибернации (спящий режим)"""
 
if __name__ == '__main__':
    try:
        import sys
        if len(sys.argv) > 1:
            seconds_delay = int(sys.argv[1])

            import time

            while seconds_delay > 0:
                print('\rDelay before hibernate: {} secs'.format(seconds_delay), end='')
                time.sleep(1)
                seconds_delay -= 1

        print('\nGo to Hibernate')

        import os
        
        # Следует заметить, что если у вас включен гибридный режим сна (Hibernate), то войдет он именно в этот режим. Отключить его можно запустив от имени администратора следующее:
        # powercfg -hibernate off
        
        # os.system('rundll32 powrprof.dll,SetSuspendState 0,1,0')
        os.system('shutdown /h /f')
        # os.system(r'%windir%\system32\rundll32.exe powrprof.dll,SetSuspendState Hibernate')

    except KeyboardInterrupt:
        print('\nInterrupt')
