import os

def read(txt, voice='Fred', speed=200):
    os.system("say -v %s %s -r %s" % (voice, txt, speed))

read("My hovercraft is full of eels.")
