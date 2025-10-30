import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
import fun_eds

lat = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'NAS-Specimen-Download.csv', 'Latitude')
long = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'NAS-Specimen-Download.csv', 'Longitude')

#print(lat)
#print(long)

#plt.plot(long, lat)
#plt.show()

plt.scatter(long, lat, s=35, color='red', marker='x', label='longitude')
plt.show()

'''year = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'NAS-Specimen-Download.csv', 'Year')

#plt.plot(year)
#plt.show()
'''