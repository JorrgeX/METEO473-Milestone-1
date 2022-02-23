# METEO473-Milestone-1
Meteo 473 Milestone 1:
The goal of this milestone is to be able to read a gridded netcdf file, specifically a Numerical Weather 
Prediction model output file from the NOAA High Resolution Rapid Refresh (HRRR) system, and extract 
meaningful information, as well as gain comfort manipulating multi-dimensional arrays.

Survival Level Tasks:
1. In your ~/meteo473/spring2022/milestone1 directory, create a ‘ms1_about.txt’ file in a similar format to 
the sample provided by the instructor.  Use this to denote group membership and final code location.
2. Read the netcdf file ‘hrrr.t18z.wrfsrc18.nc’ in Python.
3. Save the field ‘TMP_2maboveground’ to a python array. Comment on its dimensions.
4. Find the latitude and longitude of the Walker Building in State College (use the internet).
5. Determine the array indices that correspond most closely to State College (use the netcdf file).  This will 
require searching the latitude and longitude arrays from the netcdf file.
6. Write a function that takes any latitude and longitude, and returns the model-predicted surface 
conditions for that location (if the location is within the model domain).  You may use nearest neighbor 
or linear interpolation.
7. Extract the 2-meter temperature for State College, and print this to the screen.  Indicate units and 
format your answer.  Repeat for another location of your choice.
8. Create a simple line plot that shows temperature as a function of longitude as a cross section through 
approximately latitude 41 N.  Ensure the plot is well labeled.

Glory Level Tasks:
1. Display the output for other variables, particularly variables that directly impact the surface 
meteorology.  Include a description of the variable.
2. Create some other line plots and interpret your results.  Note: we will be doing multi-dimensional 
plotting / making maps in the second Milestone, so please wait until then to try these.
3. Read a text (ASCII) file that contains latitude, longitude pairs, and use the function to return surface 
conditions at all locations in the file.  Print the results to a text (ASCII) file.

Due Date:  You are encouraged to complete this milestone before class on Monday, February 21.  
Submissions will be accepted through 6:00 pm EST Tuesday, February 22 without late penalty.
