#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:19:46 2017

@author: maria
"""
from string import rstrip
import json

#Get substring from a large string starting from the offset and with a length of value
def get_substring(string, offset, value):
    substring = string[offset:(offset+value)]
    return substring.strip()

#Transform string to float
def str2float(string):
    fl = float(string)
    return fl

#Transform string to integer
def str2int(string):
    fl = int(string)
    return fl

#Transform 2-digit years to 4-digit years (e.g. 98 to 1998)
def year4dig(year2dig):
    if int(year2dig.strip("0")) < 57: year = str2int("20"+year2dig) #1957: first man-mdade satellite in space
    else: year = str2int("19"+year2dig)
    return year

#Transform format of 12345-4 to 12345e-5
def powerform(string):
    numstring = "0."+string[1:]
    if "+" in numstring: 
        pow_ind = numstring.index("+")
        power = str2float(get_substring(numstring, 0, pow_ind))*10.**(str2float(get_substring(numstring,pow_ind,2)))
    elif "-" in numstring: 
        pow_ind = numstring.index("-")
        power = str2float(get_substring(numstring, 0, pow_ind))*10.**(str2float(get_substring(numstring,pow_ind,2)))
    if string[0] == "-": power = -power       
    return power

#Transform TLE to JSON using the files above
def TLE2JSON(TLE):    
    #Set the parameters and put them in dictionary
    satellite_id = {
            "name":get_substring(TLE,0,23), 
            "number":str2int(get_substring(TLE,27,5)), 
            "classification":get_substring(TLE,32,1)}
    international_designator = {
            "launch_year":year4dig(get_substring(TLE,34,2)), 
            "launch_number_of_the_year":str2int(get_substring(TLE,37,2)), 
            "piece_of_the_launch":get_substring(TLE,39,1)}
    epoch_information = {
            "year":year4dig(get_substring(TLE,41,4)), 
            "day":str2float(get_substring(TLE,45,12))}
    mean_motion_derivatives = {
            "first_time_by_two":str2float(get_substring(TLE,58,10)), 
            "second_time_divided_by_six":powerform(get_substring(TLE,69,8))}
    bstar_drag_term = powerform(get_substring(TLE,78,8))
    element_set_number = str2int(get_substring(TLE,89,5))
    orbital_parameters = {
            "inclination":str2float(get_substring(TLE,103,8)), 
            "right_ascension_of_the_ascending_note":str2float(get_substring(TLE,112,8)), 
            "eccentricity":str2float("0."+get_substring(TLE,121,7)), 
            "argument_of_perigee":str2float(get_substring(TLE,129,8)), 
            "mean_anomaly":str2float(get_substring(TLE,138,8)), 
            "mean_motion":str2float(get_substring(TLE,147,11))}
    revolution_number_at_epoch = str2int(get_substring(TLE,158,5))
    checksum = str2int(get_substring(TLE,163,1))
    
    #Include the parameters in an overall dictionary
    record = {
            "satellite_id": satellite_id, 
            "international_designator": international_designator, 
            "epoch_information": epoch_information, 
            "mean_motion_derivatives": mean_motion_derivatives, 
            "bstar_drag_term": bstar_drag_term, 
            "element_set_number": element_set_number, 
            "orbital_parameters": orbital_parameters, 
            "revolution_number_at_epoch": revolution_number_at_epoch, 
            "checksum": checksum}
    
    return record

#Search for satellites from whitelist.txt in all.txt
def search_tle(white_list,all_list):
    #Open whitelist and make names similar to all
    with open(white_list,"r") as files:
        whitelist = map(rstrip,files)

    #Open all list:
    with open(all_list,"r") as files:
        all_tle = files.read().replace("\r","")

    #Make list and input all of the names in all which matches in whitelist
    records = [0]*len(whitelist)
    for i in range(0,len(whitelist)):
        if whitelist[i] in all_tle:
            ind = all_tle.index(whitelist[i])
            TLE = all_tle[ind:(ind+164)]
            records[i] = TLE2JSON(TLE)
    
        else: print whitelist[i], "is not in all.txt."

    return records

#Run programs to write json file
white_list = "whitelist.txt"
all_list = "all.txt"
records = search_tle(white_list,all_list)
#Make the single quotes become double quotes (requirement for json format) and save to json file
with open('data.json','w') as out:
    json.dump(records, out)
