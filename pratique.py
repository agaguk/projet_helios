#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
img = Image.open('data/soleil.jpeg').convert('L')
img.save('data/pil-greyscale.jpeg')
