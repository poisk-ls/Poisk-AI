import subprocess
import os
import time
from datetime import datetime
import sys
now = datetime.now()
t=now.strftime('%I:%M:%p')
print(t)

inp = subprocess.getoutput("termux-speech-to-text")
time.sleep(1)
print("\033[95m You said: ",str(inp))

def system():
     if inp == "":
         subprocess.call(["termux-tts-speak","please tell something commander!!"])

     elif "hello" in inp:
         subprocess.call(["termux-tts-speak","hello commander, how's your day!"])

     elif "close" in inp:
         subprocess.call(["termux-tts-speak","okay commander wait a minute"])
         time.sleep(1)
         sys.exit()
     elif "how are you" in inp:
        subprocess.call(["termux-tts-speak","i am good pro "])
     elif "battery" in inp:
         subprocess.call(["termux-battery-status"])

     elif "sleep" in inp:
         subprocess.call(["termux-tts-speak","ok pro i am going to sleep for 5 second"])
         time.sleep(5)

     elif "vibrate" in inp:
         os.system("termux-vibrate")
     elif "torch on" in inp:
         os.system("termux-torch on")
     elif "torch off" in inp:                                                                                                  os.system("termux-torch off")

     elif "YouTube" in inp:
         os.system("termux-open https://m.youtube.com")
     elif "Google" in inp:
         os.system("termux-open https://www.google.co.in/")

     elif "contact" in inp:
         os.system("termux-contact-list")

     elif "train" in inp:
         os.system("sl")
         
     elif "cow" in inp:
         os.system("cowsay")

     elif "calendar" in inp:
         os.system("cal")

     elif "matrix" in inp:
         os.system("cmatrix -b -B -u 1")

     elif "smoke" in inp:
         os.system("cacafire")

     elif "demo" in inp:
         os.system("cacademo")

     elif "system" in inp:
         os.system("neofetch")

     elif "who are you" in inp:
         subprocess.call(["termux-tts-speak","I am your virtual assistant, Terminal Commander."])

     elif "time" in inp:
         subprocess.call(["termux-tts-speak",t])

     elif "what are you doing" in inp:
        subprocess.call(["termux-tts-speak","i am busy with you "])

     elif "are you busy" in inp:
         subprocess.call(["termux-tts-speak","i am always free for you"])

     elif "name" in inp:
         subprocess.call(["termux-tts-speak","you can call me poisk-ls"])


     elif "who made you" in inp:
         subprocess.call(["termux-tts-speak","customize by poisk-ls"])
     elif "video" in inp:
         os.system("termux-open https://www.google.com/search?q=video")

     else:
       subprocess.call(["termux-tts-speak","Tell something!"])

system()

os.system("python poisk.py")