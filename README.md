# NoahJulienProject
Our EDS project

Readme file with the following components:
• Brief summary of project

• Process to generate all figures used in the presentation
Data was imported and parsed for "Year", "Latitude", and "Longitude" using pandas, which was was assigned to a variable. Then, using the bound function "min" and max", we gathered the max and min of each data point for "longitude" and "latitude" plus or minus "1", which created the dimensions of the scatter-plot. Afterwards, using module "basemap" from matplotlib, we generated a map of North America, with x and y axis that represented the latitude and longitude, plus sepereate functions which made river, lakes, coastlines, and ocean. Ontop of that map we created a scatterplot, using the outputs from the variable assigned to the longitude and latitude, from the data set. Then, we assigned the colorbar to the "Year" variable from the data set, where each plot, and the year that data was taken, would correspond to a different color. Finally, we changed the color of the colorbar to better represent the gradient of different years as well as added longitude and latitude labels to the map. 

• Index of code
fun_eds: 
wrap_eds: 
• Generative AI was not used in this code.
