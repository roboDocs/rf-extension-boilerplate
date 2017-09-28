'''build RoboFont Extension'''

import os
from AppKit import NSImage
from mojo.extensions import ExtensionBundle

# get current folder
basePath = os.path.dirname(__file__)

# get parent folder for all extension files
libPath = os.path.join(basePath, 'myExtension')

# folder with html files
htmlPath = os.path.join(libPath, 'html')

# folder with resources
resourcesPath = os.path.join(libPath, 'resources')

# boolean indicating if only .pyc should be included
pycOnly = False

# name of the compiled extension file
extensionFile = 'myExtension.roboFontExt'

# path of the compiled extension
extensionPath = os.path.join(basePath, extensionFile)

# initiate the extension builder
B = ExtensionBundle()

# name of the extension
B.name = "myExtension"

# name of the developer
B.developer = 'Python Monty'

# URL of the developer
B.developerURL = 'http://youtu.be/akbflkF_1zY'

# extension icon
imagePath = os.path.join(resourcesPath, 'icon.png')
B.icon = NSImage.alloc().initWithContentsOfFile_(imagePath)

# version of the extension
B.version = '0.1'

# should the extension be launched at start-up? 1=Yes, 0=No
B.launchAtStartUp = 1

# script to be executed when RF starts
B.mainScript = 'lib/hello.py'

# script to be executed when the extension is unistalled
B.uninstallScript = 'lib/goodbye.py'

# does the extension contain html help files? 1=Yes, 0=No
B.infoDictionary["html"] = 1

# minimum RoboFont version required for this extension
B.requiresVersionMajor = '1'
B.requiresVersionMinor = '5'

# scripts which should appear in Extensions menu
B.addToMenu = [
    {
        'path' : 'lib/doSomething.py',
        'preferredName': 'do something',
        'shortKey' : '',
    },
    {
        'path' : 'lib/doSomethingElse.py',
        'preferredName': 'do something else',
        'shortKey' : '',
    }
]

# compile and save the extension bundle
print 'building extension...',
B.save(extensionPath, libPath=libPath, htmlPath=htmlPath, resourcesPath=resourcesPath, pycOnly=pycOnly)
print 'done!'

# check for problems in the compiled extension
print
print B.validationErrors()
