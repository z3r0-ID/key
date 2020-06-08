#Created by z3r0_ID
#Github        : https://github.com/MrCimin
#mail          : skyla_term@yopmail.com
#latest update : 7-6-2020 23:39

#import session

import os, sys
from time import sleep

#banner and script system

os.system('clear')
banner='''

   \033[0;37m(_    ,_,    _)    \033[1;31mTermux \033[1;37mKeys
   \033[0;37m/ `'--) (--'` \    \033[1;36m════════════════
  \033[0;37m/  _,-'\_/'-,_  \   \033[1;32mAuthor \033[1;37m: \033[1;33mz3r0_ID
 \033[0;37m/.-' 1.2 "     '-.\  \033[1;32mGithub \033[1;37m: \033[1;33mhttps://github.com/MrCimin

'''
os.system('clear')
print(banner)
print('\033[1;37m[\033[1;32m1\033[1;37m]\033[1;33m.\033[0;35mInstall')
print('\033[1;37m[\033[1;32m2\033[1;37m]\033[1;33m.\033[0;35mExit')
print('')
print('\033[1;37m[\033[1;31mU\033[1;37m]\033[1;33m.\033[0;35mUninstall Keys')
print('\033[1;37m[\033[1;32mA\033[1;37m]\033[1;33m.\033[0;35mUpdate \033[1;30m( jika folder ada di penyimpanan termux :) )')
print('')
pil = input('\033[1;32m[\033[1;36m?\033[1;32m] \033[1;31mPilih > \033[0;37m')
if pil == '1':
  os.system('clear')
  print(banner)
  try:
    os.mkdir('/data/data/com.termux/files/home/.termux')
  except:
    pass
  key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
  open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(key)

  for i in "-\|/-\|/-\|/-\|-":
    print('\r\033[0;35mPlease \033[1;33mWait \033[1;37m['+i+'] ',end="",flush=True)
    sleep(0.1)
  os.system('termux-reload-settings')
  os.system('clear')
  print (banner)
  print('\033[1;37m[\033[1;32m√\033[1;37m] \033[1;31mSuccesfully \033[1;37mInstalled')
  print('')
  print('\033[1;37m[\033[1;31m!\033[1;37m] \033[0;35mPlease Restart Your Termux \033[1;30m( ctrl + d )')
  print('\033[1;37m')
elif pil == '2':
  print('\033[1;32m[\033[1;31mBye Bye :(\033[1;32m]')
  sleep(2.0)
  os.system('clear')
  print(banner)
  sleep(2.0)
  os.system('clear')
elif pil == 'U' or pil == 'u':
  os.system('clear')
  print(banner)
  kep = str(input('\033[1;32m[\033[1;33m?\033[1;32m] \033[1;36mYakin Mau Uninstall Tombol\033[0;31m? \033[1;37m[\033[1;33my\033[1;37m/\033[1;31mn\033[1;37m] \033[0;35m: \033[1;32m'))
  if kep == 'y' or kep == 'Y':
    os.system('clear')
    print(banner)
    for x in "-\|/-\|/-\|/":
      print('\r\033[1;33mWait... \033[1;31m'+x+' ',end="",flush=True)
      sleep(0.1)
    os.system('clear')
    os.system('sh un.sh')
    os.system('clear')
    print(banner)
    print('\033[1;37m[\033[1;31m•\033[1;37m] \033[1;32mSuccess Uninstalled')
    print('')
    print('\033[1;32m[\033[1;31m!\033[1;32m] \033[0;35mPlease restart your termux \033[1;30m( ctrl + d )')
  elif kep == 'n' or kep == 'N':
    os.system('clear')
    print(banner)
    print('\033[1;31m[!] Bye Bye')
    sleep(1.0)
    os.system('clear')
    os.system('cd $HOME')
  else:
    print('\033[1;31m[Key Interrupt]')
elif pil == 'a' or pil == 'A':
  os.system('clear')
  print(banner)
  int = str(input('\033[1;37m[\033[1;31m!\033[1;37m] \033[0;35mPerangkat terhubung ke internet? \033[1;30m[y/n] \033[1;37m: \033[1;32m'))
  if int == 'y' or int == 'Y':
    os.system('clear')
    print(banner)
    for c in "-\|/-\|/-\|/":
      print('\r\033[1;32m[\033[1;36m!\033[1;32m] \033[1;36mUpdate \033[1;32m'+c+' ',end="",flush=True)
      sleep(0.1)
    os.system('sh up.sh')
    print('\033[1;30m[\033[1;32m•\033[1;30m] \033[1;32mUpdate Success')
    print('')
    print('\033[1;37m[\033[1;31m!\033[1;30m] \033[0;35mPlease restart termux \033[1;30m( ctrl + d )')
  elif int == 'n' or int == 'N':
    os.system('clear')
    print(banner)
    print('\033[1;31m[!] Pastikan perangkatmu terhubung ke internet terlebih dahulu [!]')
    sleep(4.0)
    os.system('clear')
  else:
    print('\033[1;31m[Key Interrupt]')
    sleep(1.0)
    os.system('clear')
    print(banner)
else:
  print('\033[1;31m[!] Error Input ')
  sleep(2.0)
  os.system('clear')
