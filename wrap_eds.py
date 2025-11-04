import matplotlib.pyplot as plt
import numpy as np
import fun_eds
#Remember to also install basemap in the terminal: python -m pip install basemap
from mpl_toolkits.basemap import Basemap

path = '/Users/julienlee/Documents/ev228_data/'
fn = 'NAS-Specimen-Download.csv'

lat = fun_eds.import_get_var(path + fn, 'Latitude')
lon = fun_eds.import_get_var(path + fn, 'Longitude')
year = fun_eds.import_get_var(path + fn, 'Year')

min_lat = min(lat)
min_lon = min(lon)
max_lat = max(lat)
max_lon = max(lon)

#Code adapted from https://matplotlib.org/basemap/stable/users/mill.html
m = Basemap(projection='mill',llcrnrlat=min_lat-1,urcrnrlat=max_lat+1,\
            llcrnrlon=min_lon-1,urcrnrlon=max_lon+1,resolution='l')
m.drawcoastlines()
m.drawrivers(color='#123476')
m.fillcontinents(color='#98cd9a',lake_color="#4c80d5")
m.drawparallels(np.arange(-90.,91.,5.), labels = [True, False, False, False], fontsize = 10, linewidth = 0.01)
m.drawmeridians(np.arange(-180.,181.,5.), labels = [False, False, False, True], fontsize = 10, linewidth = 0.01)
m.drawmapboundary(fill_color='#4c80d5')
m.scatter(lon, lat, s=35, c=year, marker='x', cmap = 'copper', latlon=True)
cbar = plt.colorbar()
cbar.set_label(label="Year", size = 14, labelpad=10, y=0.47)
plt.title("Locations of Zebra Mussel Observations, 1986 to 2025", fontsize = 22.5)
plt.show()