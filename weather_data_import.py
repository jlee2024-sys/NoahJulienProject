
import matplotlib.pyplot as plt
import pandas as pd
import numpy as npcon
import scipy.stats as stats
import fun_eds

krdu = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'KRDU_temp_188708-202508.csv', 'metANN')
print(krdu)

ayw = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'AYW00090001_temp_195702-202508.csv', 'metANN')
print(ayw)

br = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'BR038014410_temp_189601-202508.csv', 'metANN')
print(br)

ind = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'IN020100400_temp_189101-202508.csv', 'metANN')
print(ind)

ksm = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'KSM00047108_temp_190710-202508.csv', 'metANN')
print(ksm)

roe = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'ROE00108901_temp_188001-202508.csv', 'metANN')
print(roe)

rsm = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'RSM00021432_temp_193601-202508.csv', 'metANN')
print(rsm)

sg = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'SG000061641_temp_189906-202508.csv', 'metANN')
print(sg)

usw = fun_eds.import_get_var('/Users/julienlee/Documents/ev228_data/', 'USW00093009_temp_190801-202508.csv', 'metANN')
print(usw)