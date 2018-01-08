# Delphini-1_W2_Exam

README JSON:
The "Project_Maria_JSON.py" is a python file which converts a given satellites TLE to JSON format and saves it as data.json. It consist of small sub-routines: 

1. get_substring(string, offset, value): Gets the substring from a large string, starting from the offset, and having a length value.

2. str2float(string): Converts a string to a float.

3. str2int(string): converts a string to an integer.

4. year4dig(year2dig): Converts a 2-digit year to a 4-digit year (will work until 2057).

5. powerform (string): Transforms the power-format in the TLE to the power-format of python and JSON.

6. TLE2JSON(TLE): Transforms a given TLE to the JSON format using the above subroutines. In the TLE a suffix of ''0.'' is implied for the eccentricity, second_time_divided_by_six and bstar_drag_term, which is taken into account. To complete the JSON format, the returned result is dumped using the JSON python package, which changes all single quotes (python) to double-quotes (JSON).

7. search_tle(white_list,all_list): searches for the satellites given in white_list in the collection of TLE's in all_list, supplied by Nestor. It returns the TLE in (almost) JSON format (only missing the change from single to double quotes, which is done afterwards, see 6.).






README Orbit calculator:
The orbit calculator takes values in the TLE given in all.txt of a given satellite in whitelist_test.txt, and makes two figures of the last orbit and a given number of future orbits, with a given timestep. It consists of small sub-routines:

1. tle(white_list,all_list): searches the all_list for the satellite given in white_list and returns the TLE.

2. lines(TLE): returns the TLE in 3 lines (name, first line and second line).

3. plot_fig(white_list,all_list,td=None,N=None,tle_time=None): plots two orbit figures of the last orbit and future orbits of a satellite given in white_list, with a TLE in all_list. Optional parameters are an orbit timestep in minutes, td (default: 1), the number of future orbits displayed, N (default: 5) and the time at which the satellite should be displayed, tle_time (default: current time). The first figure is a projection of a globe, while the second figure is the 2D mercator projection used by e.g. STK. The latitude and longitude of the satellite for a given time is calculated using the python packages ephem.py and datetime.py, since such a calculation is outside the scope of this course.
