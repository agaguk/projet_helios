# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import astropy.units as u
import sunpy.net
import sunpy.map
from sunpy.net import Fido
from sunpy.net import attrs as a
from astropy.io import fits
#-----------------------------------------------------------------------------
#   recherche des images disponibles     HMI
result = Fido.search(a.Time('2022/09/16 00:00:00', '2022/09/16 00:01:00'),
                     a.Instrument.hmi, 
#                      a.Physobs.los_magnetic_field)   # premier choix
                     a.Physobs.intensity)              # deuxieme choix
#                      a.Physobs.los_velocity)         # troisieme choix
result.show("Start Time","Source", "Instrument", "Provider","Wavelength", "Physobs","Info")
print(result)
#-----------------------------------------------------------------------------
# downloaded_files = Fido.fetch(result)
downloaded_files = Fido.fetch(result, path='data/{file}')  # inclues le  path
print(downloaded_files[0])
#-----------------------------------------------------------------------------
# 


