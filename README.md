# svg_automation_flowers
Project to further automate the manipulation of my personalized flower design.  

## Table of Contents
1.[Installation](#installation)
2.[Project Motivation](#motivation)
3.[File Descriptions](#files)
4.[Results](#results)
5.[Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

The code is written using Pythons version 3.11.0. All libraries are available within the Anaconda distribution of Python.

## Project Motivation <a name="motivation"></a>

In this project, I automated the personalization of my 3D Designs. The program completely replaces the time consuming process of changing names directly in the design and thereby makes the creation process of my personalized 3D flower pots more efficient.

## File Descriptions <a name="files"></a>

insert_names.py: Script that alters my 3D-model by inserting names from a csv-file into a svg-file, converting it to png and updating the stl of the flowerpot. 

## Results <a name="results"></a>

The following tasks are peformed by my Python script:
* Import CSV with names
* Open template and copy it to new file
* Replace name placeholder by name
* Save changes in new svg-file
* Export image to png or jpg and invert colors.
* Create stl with updated surface

### Template
![Template](./flowers_24.jpg)
### Modified Image
![Updated_Design](./flowers_24_inv.jpg)
### Modified 3D Model
![Updated_3D_Model](./3d_model_flowerpot.png)

For more information about my project please refer to my blog post on https://breuerei.de/automating-my-personalized-3d-designs-with-python/

## Licensing, Authors, Acknowledgements <a name="licensing"></a>

Please feel free to use my code for your own projects.
