import os
from mojo.UI import PostBannerNotification

def hello():
    PostBannerNotification('Hello World', informativeText='Welcome to RoboFont!')

def read(txt, voice='Fred', speed=200):
    os.system("say -v %s %s -r %s" % (voice, txt, speed))

def doSomething():
    read("I will not buy this record, it is scratched.")

def doSomethingElse():
    read("My hovercraft is full of eels.")
