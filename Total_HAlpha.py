import os
from astropy.table import QTable, Table
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import numpy.ma as ma

masterList = Table.read("F:\Research\Fall2020\masterList.txt", format = "ascii.commented_header")
for i in range(len(masterList)):
    map_filename = 'data/manga-' + masterList['galID'][i] + '-MAPS-HYB10-GAU-MILESHC.fits'
    if os.path.exists(map_filename):
        maps = fits.open(map_filename, format = 'fits')
        Ha_mask_extension = maps['EMLINE_GFLUX'].header['QUALDATA']
        masked_Ha_map = ma.array(Ha_map, mask=maps[Ha_mask_extension].data[18] > 0)
        total_Ha_flux = np.sum(masked_Ha_map)
        masterList['Total_Ha_flux'][i] = total_Ha_flux