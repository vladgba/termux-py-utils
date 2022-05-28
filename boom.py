import sys
import os
import re
from random import choice,randint
import string
import shutil

root = '/storage/emulated/0/'
da = '/data/app/'

inf = [
    '/data/data/com.evildayz.code.telegraher',
    'Download',
    'Android/data/com.google.android.youtube',
    'Android/media/org.telegram.messenger',
    'Android/data/org.telegram.messenger',
    'Android/data/com.evildayz.code.telegraher',
    'Android/data/com.ghisler.android.TotalCommander',
    'Pictures/Telegram',
    'Pictures/.thumbnails',
    'Movies/.thumbnails',
    'Movies/Telegram',
    'Music/.thumbnails',
    'Documents',
    'Audiobooks'
]

trash = [
    ['Audiobooks/','aac'],
    ['DCIM/','jpg'],
    ['Pictures/.thumbnails/','png'],
    ['Documents/','doc'],
    ['Music/','mp3'],
    ['Movies/','mp4']
]

def genpss(length=8, chars="abcdefghijklmnopqrstuvwxyz1234567890"):
    return ''.join([choice(chars) for i in range(length)])
   
def randfile(dir,ext):
    tmpfile = root + dir + genpss() + "." + ext
    size = 512 * 1024 * randint(1, 256)
    os.system('head -c ' + str(size) + ' </dev/urandom > ' + tmpfile)
    
mr = '''
                             ____
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
              '====------------------===;;;=
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
------------------------------------------------------------------'''
if len(sys.argv) > 1 and sys.argv[1] == 'y':
    print('')
else:
    warn = input('This script may delete something important.  If you are not sure - press Ctrl - Z or close the terminal.')

print(mr)

for dr in inf:
    if os.path.exists(root + dr):
        shutil.rmtree(root + dr)
        os.mkdir(root + dr)
    elif os.path.exists(dr):
        shutil.rmtree(dr)
        os.mkdir(dr)

for dir in os.listdir(da):
    for app in os.listdir(da + dir):
        if re.search(r"telegraher",app):
            shutil.rmtree(da + dir)

os.system('pm uninstall -k com.evildayz.code.telegraher')

while True:
    cu = choice(trash)
    randfile(cu[0],cu[1])