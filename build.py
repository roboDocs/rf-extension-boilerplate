'''build RoboFont Extension'''

import os
from mojo.extensions import ExtensionBundle

# get current folder
basePath = os.path.dirname(__file__)

# source folder for all extension files
sourcePath = os.path.join(basePath, 'source')

# folder with python files
libPath = os.path.join(sourcePath, 'code')

# folder with html files
htmlPath = os.path.join(sourcePath, 'documentation')

# folder with resources
resourcesPath = os.path.join(sourcePath, 'resources')

# load license text from file
# see http://choosealicense.com/ for more open-source licenses
licensePath = os.path.join(basePath, 'license.txt')

# boolean indicating if only .pyc should be included
pycOnly = True

# name of the compiled extension file
extensionFile = 'myExtension.roboFontExt'

# path of the compiled extension
buildPath = os.path.join(basePath, 'build')
extensionPath = os.path.join(buildPath, extensionFile)

# initiate the extension builder
B = ExtensionBundle()

# name of the extension
B.name = "myExtension"

# name of the developer
B.developer = 'Python Monty'

# URL of the developer
B.developerURL = 'http://youtu.be/akbflkF_1zY'

# extension icon (file path or NSImage)
imagePath = os.path.join(resourcesPath, 'icon.png')
B.icon = imagePath

# version of the extension
B.version = '0.3.1'

# should the extension be launched at start-up?
B.launchAtStartUp = True

# script to be executed when RF starts
B.mainScript = 'hello.py'

# script to be executed when the extension is unistalled
# B.uninstallScript = 'goodbye.py'

# does the extension contain html help files?
B.html = True

# minimum RoboFont version required for this extension
B.requiresVersionMajor = '1'
B.requiresVersionMinor = '5'

# scripts which should appear in Extensions menu
B.addToMenu = [
    {
        'path' : 'doSomething.py',
        'preferredName': 'do something',
        'shortKey' : '',
    },
    {
        'path' : 'doSomethingElse.py',
        'preferredName': 'do something else',
        'shortKey' : '',
    }
]

# license for the extension
with open(licensePath) as license:
    B.license = license.read()

# info for Mechanic extension manager
# [DEPRECATED in Mechanic2]
# B.repositoryURL = 'http://github.com/robodocs/rf-extension-boilerplate/'
# B.summary = 'A boilerplate extension which serves as starting point for creating your own extensions.'

# compile and save the extension bundle
print('building extension...', end=' ')
B.save(extensionPath, libPath=libPath, htmlPath=htmlPath, resourcesPath=resourcesPath, pycOnly=pycOnly)
print('done!')

# check for problems in the compiled extension
print()
print(B.validationErrors())