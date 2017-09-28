'''build RoboFont Extension'''

import os
from mojo.extensions import ExtensionBundle

# parent folder for all extension files
libPath = os.path.dirname(__file__)

# folder with html files
htmlPath = os.path.join(libPath, 'Docs')

# folder with resources
resourcesPath = None

# boolean indicating if only .pyc should be included
pycOnly = False

# name of the compiled extension file
extensionFile = 'myExtension.roboFontExt'

# path of the compiled extension
extensionPath = os.path.join(libPath, extensionFile)

# ---------------
# build extension
# ---------------

# initiate the extension builder
B = ExtensionBundle()

# name of the extension
B.name = "myExtension"

# name of the developer
B.developer = 'Developer Name'

# URL of the developer
B.developerURL = 'http://mywebsite.com/'

# version of the extension
B.version = '0.1'

# should the extension be launched at start-up? 1=Yes, 0=No
B.launchAtStartUp = 0

# 
B.mainScript = 



# does the extension contain html help files? 1=Yes, 0=No
B.infoDictionary["html"] = 1

# minimum RoboFont version required for this extension
B.requiresVersionMajor = '1'
B.requiresVersionMinor = '5'

# scripts which should appear in Extensions menu
B.addToMenu = [
    {
        'path' : 'hello.py',
        'preferredName': 'Hello World',
        'shortKey' : '',
    }
]

# compile and save the extension bundle

print 'building extension...'

B.save(extensionPath, libPath=libPath, htmlPath=htmlPath, resourcesPath=resourcesPath, pycOnly=pycOnly)

print '...done.'

# check for problems in the compiled extension

print
print B.validationErrors()

