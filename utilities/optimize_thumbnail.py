#!/usr/bin/python3

# This file creates a thumbnail for an article, which is just a smaller version
# of the image that an article references. The relative path to the image an
# article references will be written in its front matter.

### Step-by-step guide of this script: ###
# 1. Loop through all articles which are in '_posts/articles'
# 2. Read the header image path in each article's front matter
# 3. Check if the image's file name has '-thumbnail' in it; if so, continue to the
#    next article
# 4a. If not, create a smaller copy of the image aka the thumbnail
# 4b. Edit the article's front matter to point to the thumbnail's path
# 4c. Print the full paths to the article and to the thumbnail to console, which
#     will be used by the next stage of the git hook to stage the files

import re
import os

from PIL import Image
from pathlib import Path
from resizeimage import resizeimage

# File constants
pat = r"[\n\r].*path:\s*([^\n\r]*)"
types = ('*.md', '*.markdown')

# Path to project root
root = Path(os.sys.argv[1])
# Path to articles directory
p = root / "_posts/articles"
for type in types:
    for file in p.glob(type):
        with file.open() as f:
            txt = f.read()
            # Search for the `path` entry in the article's front matter
            image_path = re.search(pat, txt).group(1)
            if '-thumbnail' in image_path:
                # This article already uses a thumbnail; so move on
                continue
            # Replace `path` in the article's front matter
            save_path = '-thumbnail'.join(os.path.splitext(image_path)[:2])
            newtxt = re.sub(pat, '\n   path: ' + save_path , txt)
            with file.open('w') as f:
                f.write(newtxt)
            image_path = str(root) + image_path
            save_path = str(root) + save_path
            # Create smaller image
            img = Image.open(image_path)
            img = resizeimage.resize_width(img, 240)
            img.save(save_path, img.format)
            # Print the path to the edited MD file and the newly-created
            # thumbnail so that the hook can add the files to the commit
            print(str(file))
            print(save_path)
