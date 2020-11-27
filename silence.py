#!/usr/bin/python
'''
sys is needed for argv

pilsuc = False for importing pil
try tries to import pillow but will install via pip if it fails
pillow used for image manipulation

open method opens the base image
truetype method opens font file

if arguments passed to, join method creats text of args
else in case no args are passed to

draw method creates a draw image object using the base image

draws text

save method saves image
'''

import sys 

pilsuc = False
while pilsuc == False:
    try:
        from PIL import Image, ImageDraw, ImageFont
        pilsuc = True
    except ImportError:
        import subprocess
        subprocess.call([sys.executable, "-m", "pip", "install", "Pillow"])

img = Image.open("img.png")
font = ImageFont.truetype("LiberationSans-Regular.ttf", 68)

if len(sys.argv) > 1:
    text = "\n".join(sys.argv[1:])
else:
    print("Usage: py silence.py [text for meme] - generates \"silence crab\" meme with input text")
    sys.exit()

draw = ImageDraw.Draw(img) 

draw.text((6,60), text, fill="white", font=font) 

img.save('export.png')
