# %%
import pandas as pd
import logging
import cv2
import numpy as np
import subprocess
import bpy

# Import Names from name_list.csv
names = pd.read_csv('name_list.csv', sep=';', header=0)
logging.info('Names imported from name_list.csv')

# Replace NaN Values by empty string
names['name']=names['name'].astype('string').fillna('')
logging.info('NaN Values replaced by empty string to make not named flowers possible.')

# %%

# Copy template to new flower_24 file
open('flowers_24_new.svg', 'w').write(open('flowers_24.svg').read())


# Change names in flower_24_new.svg
with open('flowers_24_new.svg') as f: 
    data = f.read()

    for i in list(names['index']):
        index = names[names['index']==i]['index'].values[0]
        if index<10: # index is smaller than 10 a zero is added before the index to get a two digit number as string
            index = '0'+ str(index)
        else:
            index = str(index)

        # create reference string in the image which is in the form of 'name05' for example
        strtorepl = 'name' + index

        # get name that shall replace the reference string
        name_i = names[names['index']==i]['name'].values[0]

        # replcace placeholder with name from names list
        data = data.replace(strtorepl,name_i)
        logging.info(f'{strtorepl} replaced by {name_i}.')
    
    # save changes to the file
    with open('flowers_24_new.svg', 'w') as f:
        f.write(data)

    logging.info('Names are changed and saved to flowers_24_new.svg')

# %%

# open Inkscape to  save image to png

INKSCAPE_PATH = r'C:\Program Files\Inkscape\bin\inkscape.exe'  # for Windows

subprocess.run([
    INKSCAPE_PATH,
    '--export-width=4000',
    '--export-type=png',
    f'--export-filename={"flowers_24_new.png"}',
    'flowers_24_new.svg'
])

logging.info('PNG created from SVG.')

# Invert Colors in png
image = cv2.imread('flowers_24_new.png', 0)
inverted = np.invert(image)

cv2.imwrite('flowers_24_inv.jpg', inverted)

logging.info('Inverted colors in PNG.')

# %%

# Start Blender and export flower pot with new image displacement as stl.

BLENDER_PATH = r'C:\Program Files\Blender Foundation\Blender 3.6\blender.exe'  # for Windows

# Set the path to the Blender file
blend_file_path = "flowerpot.blend"
stl_output_path = "flowerpot.stl"

# Open the Blender file
bpy.ops.wm.open_mainfile(filepath=blend_file_path)

# Ensure all objects are selected for export
bpy.ops.object.select_all(action='SELECT')

# Export to STL
bpy.ops.wm.stl_export(filepath=stl_output_path)


# %%
