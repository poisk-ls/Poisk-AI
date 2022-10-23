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
         subprocess.call(["termux-tts-speak","please tell something pro"])

     elif "hello" in inp:
         subprocess.call(["termux-tts-speak","hallow pro "])
         
     elif "close" in inp:
         subprocess.call(["termux-tts-speak","ok pro wait a minute"])
         time.sleep(1)
         sys.exit()
     elif "how are you" in inp:
        subprocess.call(["termux-tts-speak","i am good pro "])
     elif "battery" in inp:
         subprocess.call(["termux-battery-status"])
         
     elif "sleep" in inp:
         subprocess.call(["termux-tts-speak","ok pro i am going to sleep for 5 second"])
         time.sleep(5)
         
     elif "call me" in inp:
         os.system("termux-telephony-call +63")
     elif "torch on" in inp:
         os.system("termux-torch on")
     elif "torch off" in inp:
         os.system("termux-torch off")
         
     elif "YouTube" in inp:
         os.system("termux-open https://m.youtube.com")
     elif "Google" in inp:
         os.system("termux-open https://www.google.co.in/")    
         
     elif "contact" in inp:
         os.system("termux-contact-list")
         
     elif "who are you" in inp:
         subprocess.call(["termux-tts-speak","I am your virtual assistanct Termux, pro"])
         
     elif "time" in inp:
         subprocess.call(["termux-tts-speak",t])
         
     elif "what are you doing" in inp:
        subprocess.call(["termux-tts-speak","i am busy with you "])
        
     elif "are you busy" in inp:
         subprocess.call(["termux-tts-speak","i am always free for you"])
     
     elif "name" in inp:
         subprocess.call(["termux-tts-speak","you can call me glyza "])
     
     
     elif "who made you" in inp:
         subprocess.call(["termux-tts-speak","customize by jade the pro"])
     elif "video" in inp:
         os.system("termux-open https://www.google.com/search?q=video")
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     else:
       subprocess.call(["termux-tts-speak","I Love You Jade"])

system()

os.system("python main.py")
