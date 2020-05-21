#Created by MrCimin
#Github : https://github.com/MrCimin
#mail   : skyla_term@yopmail.com

#import session

import os, sys
from time import sleep

#color

r ='\033[1;31m'
b ='\033[1;34m'
y ='\033[1;33m'
g ='\033[1;32m'
c ='\033[1;36m'
m ='\033[0;35m'

#banner and script system

os.system('clear')
banner='''

   \033[0;37m(_    ,_,    _)    \033[1;31mTermux \033[1;37mKeys
   \033[0;37m/ `'--) (--'` \    \033[1;36m════════════════
  \033[0;37m/  _,-'\_/'-,_  \   \033[1;32mAuthor \033[1;37m: \033[1;33mMrCimin
 \033[0;37m/.-' 1.0 "     '-.\  \033[1;32mGithub \033[1;37m: \033[1;33mhttps://github.com/MrCimin

'''

print(banner)
try:
  os.mkdir('/data/data/com.termux/files/home/.termux')
except:
  pass
key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(key)

for i in "-\|/-\|/":
  print('\r\033[1;31mPlease \033[1;37mwait '+i+' ',end="",flush=True)
  sleep(0.2)
os.system('termux-reload-settings')
os.system('clear')
print (banner)
print('\033[1;37m[\033[1;32m√\033[1;37m] \033[1;31mSuccesfully \033[1;37mInstalled')
print('')
print('\033[1;37m[\033[1;31m!\033[1;37m] \033[0;35mPlease Restart Your Termux \033[1;30m( ctrl + d )')
print('\033[1;37m')

