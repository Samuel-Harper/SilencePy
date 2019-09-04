#!/usr/bin/python

import sys #sys used for argv

pilsuc = False #flag for import of pil
while pilsuc == False:
    try:#try import pillow, if it fails installs through pip
        from PIL import Image, ImageDraw, ImageFont #pillow used for image manipulation
        pilsuc = True
    except ImportError:
        import subprocess
        subprocess.call([sys.executable, "-m", "pip", "install", "Pillow"])


img = Image.open("img.png")#opens base image
font = ImageFont.truetype("LiberationSans-Regular.ttf", 68)#opens font file

if len(sys.argv) > 1:#if arguments
    text = "\n".join(sys.argv[1:])#creates text of args
else:#if no args exits
    print("Usage: py silence.py [text for meme] - generates \"silence crab\" meme with input text")
    sys.exit()

draw = ImageDraw.Draw(img) #creates draw image object with base image

draw.text((6,60), text, fill="white", font=font) #draws text 

img.save('export.png') #saves image