##Boxuan Xia final project
##bird migration visualization

''''first way to store long,lat and id to different list '''''
####read the data
##data_file = open(r"C:\Users\JeremyXia\Dropbox\Graduate\GIS5578\final project\ABS.csv")
####Creating two empty list for longtitude and latitude 
##latitude = [] 
##longtitude = []
####list for sample ID
##sampleID = []
####store the lat and long and sample id to separate list, split by ","
##for index, line in enumerate(data_file.readlines()):
##    if index > 1:
##        latitude.append(float(line.split(',')[4]))  ## latitute is on the 5th cols 
##        longtitude.append(float(line.split(',')[3])) ## Longtitude is on the 4th cols 
##        sampleID.append(str(line.split(',')[6]))  ## sample Id is on the 7th cols

''''second way to do it by using the pandas module''''

import pandas as pd
df = pd.read_csv(r"E:\work\Argentine Barn Swallows-tracks.csv")     
longtitude = df['location-long'].values.tolist()   ##convert selected column to a list
latitude = df['location-lat'].values.tolist()
lampleID = df['tag-local-identifier'].values.tolist()

        
'''''''building the map''''''' 

##import basemap module,so basemap will shows in the background
from mpl_toolkits.basemap import Basemap
#import the matplotlib module to plot the data on the canvas
import matplotlib.pyplot as plt
import numpy as np

##set up the basemap for background :set up the extend for study area, which is South America
##set up the projection for the map which is the web mecator that project angles. 
##
map = Basemap(llcrnrlon=-100., llcrnrlat=-45.,urcrnrlon=-20.,urcrnrlat=20.,
            projection='merc',lat_1=-50.,lat_2=20.,lon_0=-70.,
            resolution ='h',area_thresh=1000.)
##draw coast lines on the map
map.drawcoastlines()
## draw the countries lines
map.drawcountries()
## fill the continent with customize color
map.fillcontinents(color = 'DarkGrey')
## draw map boundaries
map.drawmapboundary()

## creating a funcition that call each sample and set it different color
def get_marker_color(sampleID):
    if sampleID == 'H974':
        return ('go')
    elif sampleID == 'H976':
        return ('yo')
    elif sampleID == 'H978':
        return ('bo')
    elif sampleID == 'H980':
        return ('co')
    elif sampleID == 'H982':
        return ('wo')
    elif sampleID == 'H987':
        return ('ko')
    elif sampleID == 'H988':
        return ('mo')
    elif sampleID == 'H989':
        return ('bo')
    else:
        return ('ro')

#x,y = map(lons, lats)
#map.plot(x, y, 'ro', markersize=2.5)

'''''plot data on the map'''''
## for loop that zip the lat, long, and ID together
for lon, lat, ID in zip(longtitude, latitude, sampleID):
    ##creating the coordinate
    x,y = map(lon, lat)
    ##set the dot size
    msize = 2
    ##set sample to different color by calling the color function
    marker_string = get_marker_color(ID)
    ##plot it on the map
    map.plot(x, y, marker_string, markersize=msize)
'''''show the result for visualization''''' 
##add title for the map
title_string = "Argentine Barn Swallows migration path"
plt.title(title_string)
plt.show()





