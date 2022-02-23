# METEO 473 Milestone 1
# Written by Yuan-Chih Hsieh, Sufyan Sartawi

import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

# read netcdf file
ncfile = nc.Dataset("/home/meteo/sjg213/meteo473/spring2022/hrrr.t18z.wrfsrc18.nc", 'r')

# temperature for 2m above the ground
temp2m = ncfile.variables["TMP_2maboveground"]
print("TMP_2maboveground's shape:", temp2m.shape) # (time, y, x) = (1, 453, 495)

# Walker building coordinates:
latitude = 40.7932 # North
longitude = 77.8670 # West

# latitude and longitude arrays
lat = ncfile.variables["latitude"]
long = ncfile.variables["longitude"]


# function to determine the surface condition for given latitude and longitude indices using binary search
# this function will only determine the index for given latitude and longitude values!!!
def surface_condition(lat1, long1):
    lat_index = 0 # index for desired latitude
    lat_upper = 453 # upper bound
    lat_mid_index = 453 // 2 # middle index of the array
    lat_lower = 0 # lower bound
    
    while lat_mid_index != lat_lower:
        # modify lower bound if mid-index is greater
        if lat1 > lat[lat_mid_index][0]:
            lat_lower  = lat_mid_index
        # modify upper bound if mid-index is smaller
        else:
            lat_upper = lat_mid_index
            
        # update the mid-index every iteration
        lat_mid_index = (lat_lower + lat_upper) // 2
    
    # decide if it is closer to upper or lower bound
    lat_index = lat_lower if (latitude - lat[lat_lower][0] < lat[lat_upper][1] - latitude) else lat_upper   


    # same logic as above (binary search)
    long_index = 0 # index for desired longitude
    long_upper = 495 # upper bound
    long_mid_index = 495 // 2 # middle index of the array
    long_lower = 0 # lower bound
    
    while long_mid_index != long_lower:
        if long1 > (360 - long[long_mid_index][1]):
            long_lower = long_mid_index
        else:
            long_upper = long_mid_index
        
        long_mid_index = (long_lower + long_upper) // 2

    # decide if it is closer to upper or lower bound
    long_index = long_lower if (longitude - (360 - long[long_lower][0]) < (360 - long[long_upper][1]) - longitude) else long_upper
    
    return  (lat_index, long_index)


# print the latitude and longitude for Walker building
lat_index, long_index = surface_condition(latitude, longitude)
print("Walker building index (latitude, longitude):", lat_index, long_index)    

# State College 2-meters temperature
print("2-meters temperature for State College:", temp2m[0, long_index, lat_index], "K")

# 2-meter dew point temperature
# The dew point temperature is an important varibale because it indicates the amount of moisture in our atmosphere
dpt2m = ncfile.variables["DPT_2maboveground"]
print("2-meters dew point temperature for State College:", dpt2m[0, long_index, lat_index], "K")

# Coordinates for Altoona
lat_altoona, long_altoona = surface_condition(40.52177, 78.40874)
print("2-meters temperature for Altoona:", temp2m[0, long_altoona, lat_altoona], "K")
print("2-meters dew point temperature for Altoona:", dpt2m[0, long_altoona, lat_altoona], "K")

# finding index for latitude 41 north
# same logic as the function above
lat41_index = 0
lat41_upper = 495 
lat41_mid_index = 495 // 2
lat41_lower = 0

while lat41_mid_index != lat41_lower:
    if 41 > lat[lat41_mid_index][0]:
        lat41_lower = lat41_mid_index
    else:
        lat41_upper = lat41_mid_index
        
    lat41_mid_index = (lat41_upper + lat41_lower) // 2
    
lat41_index = lat41_lower if (41 - lat[lat41_lower][0]) < (lat[lat41_upper][1] - 41) else lat41_upper


# plotting temperature map for 41N
plot_long = [] # store longitude values
plot_temp = [] # store temperature values
plot_dpt = [] # store dew point temperature values
for i in range(temp2m.shape[1]):
    plot_long.append(360 - long[i, lat41_index])
    plot_temp.append(temp2m[0, i, lat41_index])
    plot_dpt.append(dpt2m[0, i, lat41_index])
    
plt.plot(plot_long, plot_temp, label='Temp', color='blue')     
plt.plot(plot_long, plot_dpt, label='DPT', color='red')

plt.xlabel('Longitude')
plt.ylabel('Temperature  (K)')
plt.title('Temperature through latitude 41N')
plt.legend()
plt.show()


# read a text file containes latitude and longitude pairs
with open("data_read.txt", "r") as r:
    names = [] # store the location name
    longs = [] # store location longitude
    lats = [] # store location latitude
    for line in r.readlines():
        # find : index
        col = line.find(':')
        names.append(line[:col])
        # find , index
        com = line.find(',')
        lats.append(float(line[col+2:com]))
        # find ) index
        par = line.find(')')
        longs.append(float(line[com+1:par]))

with open("data_write.txt", "w") as w:
    for i in range(len(names)):
        # find lat, long index first then get the temperature values
        lat_index, long_index = surface_condition(lats[i], longs[i])
        w.write(str(names[i])+'('+str(lats[i])+','+str(longs[i])+') --> '+'Temp: '+str(temp2m[0,long_index,lat_index])+'K, '+'DPT: '+str(dpt2m[0,long_index,lat_index])+'K'+'\n')

print("Surface conditions at several loactions have been written into 'data_write.txt'.")
