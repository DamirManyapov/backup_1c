#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Backup 1C Bases and upload arhive to Cloud disk

import os
import time
import zipfile
import datetime
import platform
#import easywebdav

# TODO сделать автоматические выбор базы, либо поиск по файлам ibases.v8i или явное 
# TODO пока делаем явное указание файла 1С.

# Определения типа ос 

OS = platform.system()
# print(OS)
if OS == 'Darwin' :
 print('MAC OS')
 ibases = os.path.expandvars('$HOME') + '/.1C/1cestart/ibases.v8i'

# Для MAC OS

#ibases = os.path.expandvars('$HOME') + '/.1C/1cestart/ibases.v8i'

print("---------------------------------------------------------------")
print("Файл настроек баз 1С найден" )
print(ibases)
print("---------------------------------------------------------------")


f = open(ibases, 'r')

print(f.read())    



#DAYS = 5        # Maximal age or file to stay, older will be deleted 

#starttime = datetime.datetime.now()
#starttime = starttime.strftime("%d.%m.%Y")

#BASE_1C = '/Users/damir/Downloads/barkon/1C_base/1CAutoservice/1Cv8.1CD'
#TMP_DIR = '/Users/damir/Downloads/barkon/1C_base/'
#TMP_ZIP = TMP_DIR + starttime +  '.zip'



# TODO Архивирование средствами Python


#jungle_zip = zipfile.ZipFile(TMP_ZIP, 'w')
#jungle_zip.write(BASE_1C, compress_type=zipfile.ZIP_DEFLATED)
 
#jungle_zip.close()

#print (TMP_ZIP)


#os.system(f'duck --upload davs://webdav.yandex.ru/ {TMP_ZIP} -u mikrotik@ippd.ru -p ******* -e overwrite')
#os.system('duck -ls davs://webdav.yandex.ru/ -u mikrotik@ippd.ru -u *********')