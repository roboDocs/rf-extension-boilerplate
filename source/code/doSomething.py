import os

def read(txt, voice='Fred', speed=200):
    os.system("say -v %s %s -r %s" % (voice, txt, speed))

read("I will not buy this record, it is scratched.")
