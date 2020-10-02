import os
from astropy.table import QTable, Table
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import numpy.ma as ma

#masterList = Table.read("masterList.txt", format = "ascii.commented_header")
masterList = Table.read("master_list_full.txt", format = 'ascii.commented_header')
masterList['Total_Ha_flux'] = np.NaN*np.ones(len(masterList), dtype = float)
print('test1')
for i in range(len(masterList)):
    map_filename = '/scratch/kdougla7/data/SDSS/MaNGA-DR16/HYB10-GAU-MILESHC/' + str(masterList['MaNGA_plate'][i]) + '/' + str(masterList['MaNGA_IFU'][i]) + '/manga-' + masterList['galID'][i]+ '-MAPS-HYB10-GAU-MILESHC.fits.gz'
    if os.path.exists(map_filename):
        maps = fits.open(map_filename, format = 'fits')
        Ha_mask_extension = maps['EMLINE_GFLUX'].header['QUALDATA']
        Ha_map = maps["EMLINE_GFLUX"].data[18]
        masked_Ha_map = ma.array(Ha_map, mask=maps[Ha_mask_extension].data[18] > 0)
        total_Ha_flux = np.nansum(masked_Ha_map)
        masterList['Total_Ha_flux'][i] = total_Ha_flux

masterList.write("masterList_all.txt", format = "ascii.commented_header", overwrite = True)
