#-------------------------------------------------------------------------------
"""
Makes folders for all rasters in a folder
"""
#-------------------------------------------------------------------------------
import os
import arcpy

# get the folder containing all of the rasters
data_folder = arcpy.GetParameterAsText(0)

# get the output folder
output_folder = arcpy.GetParameterAsText(1)

#get the number of characters in the extension name
extnum = arcpy.GetParameterAsText(2)

# set the workspace to the inputted folder
arcpy.env.workspace = data_folder
basefolder = output_folder + "\\"

# Produce a list of all rasters in the parent folder
rast_list = arcpy.ListRasters()
list_len = len(rast_list)

# Create the folders from the list
arcpy.SetProgressor('step', "Converting raster", 0, list_len, 1)
for item in rast_list:
    #Remove the extensions from the raster names
    rastpath = basefolder + (str(item)[:- int(extnum)])
    # create the folder
    os.mkdir(rastpath)
    # update the progression bar with each created folder
    arcpy.SetProgressorPosition()



