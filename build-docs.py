import os
import markdown
from markdown.extensions.toc import TocExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension

# print(markdown.__version__) # 3.1.1

folderBase  = os.getcwd()
indexSource = os.path.join(folderBase, 'source', 'documentation', 'index.md')
indexBuild  = os.path.join(folderBase, 'build', 'myExtension.roboFontExt', 'html', 'index2.html')

htmlTemplate = '''\
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>%s</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
%s
</body>
</html>
'''

with open(indexSource, mode="r", encoding="utf-8") as f:
    mdSource = f.read()

M = markdown.Markdown(extensions=[
        TocExtension(permalink=True, toc_depth='2-3'),
        TableExtension(),
        FencedCodeExtension(),
        CodeHiliteExtension(),
    ])
html = htmlTemplate % ('MyExtension', M.convert(mdSource))

with open(indexBuild, mode="w", encoding="utf-8") as f:
    f.write(html)
