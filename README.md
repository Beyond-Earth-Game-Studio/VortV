# VortV
VortV is an in-development game engine written in Python using [PySide6](https://doc.qt.io/qtforpython-6/quickstart.html)

## Installation
Executables are provided every tagged pre-release. Run at your own risk and be ready for bugs.  

Full installers will be provided when we have more of a finished product.

## Building from source
Packages are built with [pyside6-deploy](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html), with resources compiled using [pyside6-rcc](https://doc.qt.io/qtforpython-6/tools/pyside-rcc.html)
### Instructions (bash)
Clone this repo and create a virtual environment in the repo root (or not, your preference)
```
mkdir venv && python3 -m venv venv
```
Activate your venv
```
source venv/bin/activate
```
Install dependancies
```
pip install pyside6
```
Switch to the source directory
```
cd src
```
Compile resources
```
pyside6-rcc resources.qrc -o resources.py
```
Build! (remember to customize your [pysidedeploy.spec](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html#pysidedeploy-spec))
```
pyside6-deploy
```

## FAQ:
- Q: Does this work?
- A: Uh, mostly? Get ready for lots of breaking changes with zero warning :)
- Q: Can I contribute?
- A: No
- Q: Why?
- A: Uh idk go bother someone else
- Q: Why are you doing this?
- A: haha funny
- Q: Why did you make your own modules and create an overcomplicated import hierarchy?
- A: haha funny
- Q: Why are you you using Qt and Python???
- A: haha funny
- Q: Why is this code hot garbage?
- A: haha funny
- Q: Why is this not memory safe?????????
- A: haha funny
- Q: This isn't funny anymore...
- A: ***HAHAHAHAHAHA FUNNY***

© 2024 Beyond Earth Studios. All rights reserved.
