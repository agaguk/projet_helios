#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
#%matplotlib inline
from astropy.wcs import WCS
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
from astropy.utils.data import download_file

filename = get_pkg_data_filename('galactic_center/gc_msx_e.fits')
#image_file = download_file('data/hmi_ic_45s_2022_09_16_00_01_30_tai_continuum.fits', cache=True )
hdu = fits.open(filename)[0]
wcs = WCS(hdu.header)

#plt.subplot(projection=wcs)
plt.imshow(hdu.data, vmin=-2.e-5, vmax=2.e-4, origin='lower')
#plt.grid(color='white', ls='solid')
#plt.xlabel('Galactic Longitude')
#plt.ylabel('Galactic Latitude')
