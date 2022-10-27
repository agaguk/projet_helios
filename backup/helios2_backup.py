# -*- coding: utf-8 -*-

import os
import glob2
import cv2
import PIL
from PIL import Image              #  pour rotation
import numpy as np
import matplotlib.pyplot as plt    #  pour visualisation  image
import matplotlib.image as mpimg
import matplotlib.colors as colors
import astropy.units as u
from astropy.io import fits
from astropy.utils.data import download_file
import numpy as np   
from math import sin, pi
import datetime                    #  pour utiliser l heure
import calendar                    #  pour utiliser date
import time
import sunpy.net
import sunpy.map
from sunpy.net import Fido
from sunpy.net import attrs as a
#from tkinter import *   

localtime = time.asctime(time.localtime(time.time()))
# -------------------------------------------------------
# faire dictionnaire pour le fun
helios_dict = { 'programmer': 'Richard',
                 'liste_aia': [],
                 'liste_hmi': [],
               'liste_autre': []}
#print('programmer = ',helios_dict.get('programmer'))
#---------------------------------------------------------
class helios:
    
    def __init__(self):
        
        self.image               = 'data/soleil.jpeg'   # sert pour des tests
        self.programmer          = 'Richard'      # nom
        self.date                = localtime      # 
        self.liste_aia           = []
        self.liste_hmi           = []
        self.liste_autre         = []
        self.liste_aia_nombre    = 0              # liste_aia nombre
        self.liste_hmi_nombre    = 0              # liste_hmi nombre
        self.liste_autre_nombre  = 0              # liste_autre nombre
        self.premier_step()                       # génère parrametres de base



    def premier_step(self):
        print("localtime = ",self.date)
        self.liste_aia = glob2.glob("data/aia*")
        self.liste_hmi = glob2.glob("data/hmi*")
        self.liste_autre = glob2.glob("data/[!ah]*")
        self.liste_aia_nombre = len(self.liste_aia)
        self.liste_hmi_nombre = len(self.liste_hmi)
        self.liste_autre_nombre = len(self.liste_autre)
        #print("liste_aia    ",self.liste_aia_nombre)     # test liste AIA
        #print("liste_hmi    ",self.liste_hmi_nombre)     # test liste HMI
        #print("liste_autre  ",self.liste_autre_nombre)   # test liste autre
        print()
        return
    
    def telecharger(self):                                # telecharge les file.FITS
        #print('richard is the best')
        return

    def display_image(self,image):                        # display image 2D numpy
        print('passe by display_image)
        #image_data,hdu_data = fits.getdata(image, header=True) 
        fig = plt.figure(figsize = (4,4))
        #plt.vmin = 0                       
        #plt.vmax = 255 
        #plt.title('test de titre')
        #plt.legend('test legend')
        #plt.xlabel('test axe X')
        #plt.ylabel('test axe y')
        plt.imshow(image, cmap='gray' )                                        
        #plt.colorbar()
        return
    
    def display_header(self,hdu_info):               #  display HDU.FITS
        print('passe par display_header')
        data,hdu_data = fits.getdata(hdu_info, header=True) 
        print(hdu_data)        
        return
    def convertir_gris(image):                       # convertie une image en gris     
        img = Image.open(image).convert('L')
        #img.save('data/greyscale2.jpeg')
        return
    
    def convertir_norm(self,liste):                  # travail sur les liste
        print('passe par convertir_norm')
        #smap = sunpy.map.Map(image)
        #smap.plot_settings['cmap'] = plt.cm.gray_r  
        fig = plt.figure(figsize=(4,4))
        #smap.plot(norm=colors.Normalize(), title='Linear normalization')
        #smap.plot(norm=colors.LogNorm(), title='Logarithmic normalization')
        #plt.colorbar()
        #plt.show()        
        return image
    
    def traite_liste(self,liste):  
        print('passe par traite_liste')
        for image in liste:
           image_data = fits.getdata(image, header= False)   # creer un 2-D numpy array
           #helios.display_image(mon_premier,image_data)      # display image en gris
           image_norm = helios.creer_norm(mon_premier,image_data)         # créer image en gris normalisée
           time.sleep(5)                                     # delay de 5 sec
           print( 'pass retour de creer_norm')           
        return


if __name__ == '__main__':
    
    #image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )  # utilisé pour testing  
    #liste_aia,liste_hmi,liste_autre =[],[],[]              #  utilisé pour testing
    image ='data/soleil.jpeg'
    mon_premier    = helios()                                       # initialiser la class
    #preparation   = helios.premier_step(mon_premier)               # test télécharger les données
    #mode_gris      = helios.convertir_gris(mon_premier,mon_premier.liste_aia) # test image en gris
    #mode_display  = helios.display_fits(mon_premier,image_file)    # test display image
    #mode_hdu      = helios.display_header(mon_premier,image_file)  # test display header
    #mode_norm     = helios.convertir_norm(mon_premier,image_file)      # test creer normalisation
    mode_liste     = helios.traite_liste(image)# convertie une image en gris
    #print('liste_aia test   ',mon_premier.liste_aia)