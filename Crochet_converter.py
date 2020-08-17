#
#Crochet Gauge Converter
#Measurements (10 stitches, 5 rows)
"""
D: length--> 6.5 cm
    width--> 3.6 cm

E: length--> 6.8 cm
    width--> 3.8 cm

F:length-->7.1 cm
    width--> 4.0 cm

G:length--> 7.3 cm
    width--> 4.0 cm

H: length--> 7.8 cm
     width--> 4.1 cm

I length--> 8.2 cm
    width--> 4.1 cm

J: length--> 8.8 cm
 width --> 4.2 cm

K: length--> 9.1 cm
    width--> 4.4 cm
    """
d_length=6.5
d_width=3.6

e_length=6.8
e_width=3.8

f_length=7.1
f_width=4.0

g_length= 7.3
g_width=4.0 

h_length=7.8
h_width=4.1

i_length=8.2 
i_width=4.1 

j_length=8.8 
j_width= 4.2

k_length=9.1 
k_width=4.4 


#Find the unit measure for old hook
def find_unit_length(hook, length):
    """find the measurements for each stitch"""

    unit_length= length/10 
    print ("The unit length of" + hook + "hook is" + unit_length)

    return unit_length

def find_unit_width(hook, width):
    """find the measurements for each row"""

    unit_width= width/5
    print ("The unit width of " + hook + "hook is" + unit_width)

    return unit_width

#Multiply unit measure of old hook by total Rows/stitches of whole project
#to find the measurements of project

def find_project_length(total_stitches):
    """find the project measurements"""
    project_length= find_unit_length(hook, length) *total_stitches #probably wrong

    return project_length

def find_project_width(total_rows):
    project_width= find_unit_width(hook, width)*total_rows

    return project_width

#Divide total project measurements by new hook unit measurements
# to find new rows and stitches

def find_new_rows(new_unit_width):
    new_rows= find_project_width(total_rows)/new_unit_width

    return new_rows

def find_new_stitches(new_unit_length):
    new_num_stitches= find_project_length(total stitches)/new_unit_length

    return new_num_stitches


