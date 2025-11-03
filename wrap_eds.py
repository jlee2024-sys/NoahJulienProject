import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
import fun_eds
import matplotlib as mpl
#Remember to also install basemap in the terminal: python -m pip install basemap
from mpl_toolkits.basemap import Basemap

lat = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'NAS-Specimen-Download.csv', 'Latitude')
lon = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'NAS-Specimen-Download.csv', 'Longitude')

min_lat = min(lat)
min_lon = min(lon)
max_lat = max(lat)
max_lon = max(lon)

'''plt.scatter(lon, lat, s=35, color='red', marker='x', label='longitude')
plt.show()
'''

#Code adapted from https://matplotlib.org/basemap/stable/users/mill.html
m = Basemap(projection='mill',llcrnrlat=min_lat-1,urcrnrlat=max_lat+1,\
            llcrnrlon=min_lon-1,urcrnrlon=max_lon+1,resolution='l')
m.drawcoastlines()
m.drawrivers(color='#123476')
m.fillcontinents(color='#98cd9a',lake_color='#4c80d5')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))
m.drawmapboundary(fill_color='#4c80d5')
m.scatter(lon, lat, s=35, color='#831d1d', marker='x', latlon=True)
plt.title("Locations of Zebra Mussel Observations, 1986 to 2025")
plt.show()

'''year = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'NAS-Specimen-Download.csv', 'Year')
print(min(year))
print(max(year))'''