# %%
from cairosvg import svg2png
import pandas as pd

# %%

# Import Names from name_list.csv
names = pd.read_csv('name_list.csv', sep=';', header=0)

names['name']=names['name'].astype('string').fillna('')
names.info()

# %%
import re

# Copy template to new flower_24 file
open('flowers_24_new.svg', 'w').write(open('flowers_24.svg').read())

with open('flowers_24_new.svg') as f:
    data = f.read()
    for i in list(names['index']):
        index = names[names['index']==i]['index'].values[0]
        if index<10:
            index = '0'+ str(index)
        else:
            index = str(index)

        strtorepl = 'name' + index
        name_i = names[names['index']==i]['name'].values[0]
        print(name_i)
        print(strtorepl)
        data = data.replace(strtorepl,name_i)
    
    with open('flowers_24_new.svg', 'w') as f:
        f.write(data)

# %%

#Create PNG
#svg2png(bytestring=open('flowers_24_new.svg').read(),write_to='flowers_24_new.png')

import aspose.words as aw

doc = aw.Document()
builder = aw.DocumentBuilder(doc)
shape = builder.insert_image("flowers_24_new.svg")
shape.get_shape_renderer().save("flowers_24_new.png", aw.saving.ImageSaveOptions(aw.SaveFormat.PNG))

# Invert Colors

import cv2
import numpy as np

image = cv2.imread('flowers_24_new.png', 0)
inverted = np.invert(image)

cv2.imwrite('flowers_24_inv.jpg', inverted)

# %%
