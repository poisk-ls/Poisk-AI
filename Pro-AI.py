import time
import datetime
import os
import subprocess



os.system('neofetch')
print('\033[1m' + '\033[91m'+'     ///   customize by poisk-ls   ///')
def wish():
  h=int(datetime.datetime.now().hour)
  if h<12:
     subprocess.call(["termux-tts-speak","Good morning pro","how may i help you"])
  else:
     if h>=12 and h<17:
       subprocess.call(["termux-tts-speak","good afternoon pro","how may i help you"])
     elif h>=17 and h<20:
       subprocess.call(["termux-tts-speak","good evening pro,how may i help you"])
     else:
       subprocess.call(["termux-tts-speak","welcome pro how may i help you"])
wish()
os.system("python main.py")
