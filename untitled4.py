#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import PIL
from PIL import Image
import matplotlib.pyplot as plt 
def grayscale(picture):
    res=PIL.Image.new(picture.mode, picture.size)
    width, height = picture.size

    for i in range(0, width):
        for j in range(0, height):
            pixel=picture.getpixel((i,j))
            avg=(pixel[0]+pixel[1]+pixel[2])/3
            res.putpixel((i,j),(avg,avg,avg))
    res.show()

image_fp = r'data/soleil.jpeg'
im = Image.open(image_fp)
grayscale(im)
