#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PIL import Image, ImageEnhance

img = Image.open("data/soleil.jpeg")
img_data = img.getdata()

lst=[]
for i in img_data:

     lst.append(i[0]*0.299+i[1]*0.587+i[2]*0.114) ### Rec. 609-7 weights
    #lst.append(i[0]*0.2125+i[1]*0.7174+i[2]*0.0721) ### Rec. 709-6 weights

new_img = Image.new("L", img.size)
new_img.putdata(lst)
new_img.show()

