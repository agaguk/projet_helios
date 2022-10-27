#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import PIL
from PIL import Image
import matplotlib.pyplot as plt 
#im = cv2.imread('data/soleil.jpeg')
im = Image.open('data/soleil.jpeg')
width, height = im.size
#height = im.size[0]                    # extract height et width
#width  = im.size[1] 
im_new = PIL.Image.new("RGB", (width,height), "white")
pixels = im_new.load()
print(width,height)
for i in range(width):
  for j in range(height):
      pixel = im.getpixel((i,j))          # Get Pixel
 # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]
      gray = (red * 0.299) + (green * 0.587) + (blue * 0.114) # Transform to grayscale # Rec. 609-7 weights
      #gray = (red * 0.299) + (green * 0.7174) + (blue * 0.0721) # Transform to grayscale Rec. 709-6 weights
      pixels[i, j] = (int(gray), int(gray), int(gray))  # Set Pixel in new image
im_new.save('data/pil-greyscale_new2.png')    