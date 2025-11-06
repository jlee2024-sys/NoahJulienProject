# NoahJulienProject

Project summary:
Our project takes data on observations of invasive zebra mussels from the United States Geological Survey's Nonindigenous Aquatic Species Database and visualizes it through a combined map and scatterplot. It outputs a map of the relevant region of North America, complete with major waterways, overlayed by the locations of the mussel observations. The observation markers are also color-coded by year to show the spread of zebra mussels over time.

Process to generate figures:
Data was imported and parsed for "Year", "Latitude", and "Longitude" using pandas, which was was assigned to a variable. Then, using the bound functions "min" and max", we gathered the max and min of each data point for "longitude" and "latitude" plus or minus "1", which created the dimensions of the scatter-plot. Afterwards, using module "basemap" from matplotlib, we generated a map of North America, with x and y axis that represented the latitude and longitude, plus separate functions which made river, lakes, coastlines, and ocean. On top of that map we created a scatterplot, using the outputs from the variable assigned to the longitude and latitude, from the dataset. Then, we assigned the colorbar to the "Year" variable from the dataset, where each plot, and the year that data was taken, would correspond to a different color. Finally, we changed the color of the colorbar to better represent the gradient of different years as well as adding longitude and latitude labels to the map. 

Index of code:
• fun_eds: contains the import_get_var() function which imports a csv file and extracts the data for a specified variable.
• wrap_eds: plots a scatterplot of zebra mussel observations over a map of North America, with a colorbar representing time.

Generative AI was not used in this code.
