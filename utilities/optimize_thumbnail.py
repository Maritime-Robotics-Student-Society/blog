import re
import os

from PIL import Image
from pathlib import Path
from resizeimage import resizeimage

pat = r"[\n\r].*path:\s*([^\n\r]*)"
types = ('*.md', '*.markdown')

p = Path("../_posts/articles")
for type in types:
    for file in p.glob(type):
        with file.open() as f:
            txt = f.read()
            image_path = re.search(pat, txt).group(1)
            save_path = (os.path.splitext(image_path)[0] + '-thumbnail' + os.path.splitext(image_path)[1])
            newtxt = re.sub(pat, '\n   path: ' + save_path , txt)
            with file.open('w') as f:
                f.write(newtxt)
            img = Image.open('..' + image_path)
            img = resizeimage.resize_width(img, 200)
            img.save('..' + save_path, img.format)
