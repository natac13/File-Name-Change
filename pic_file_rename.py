#!/usr/bin/env python3

# the above is so I can place the python file in usr/local/bin and have it
# sudo chmod 775 so that it can be executed from anywhere

import os   # work with the operating system
import re   # work with substitute
# first change the working directory
os.chdir("/home/natac/Pictures")    # could be different

print(os.getcwd())  # check working directory.


def pic_file_rename(description, date, execute=False):

    # description is new prefix to file. This is a general title
    # date is a string: the MOST important parameter since it is the search
    # for the picture files in the directory
    # execute is to preview the change to make sure things are the way I want
    # returns: nothing

    index = 1
    for pic in os.listdir('.'):
        if pic.startswith(date):
            new = description + pic[:8] + "_" + str(index) + pic[-4:]
            index += 1
            if execute:
                os.rename(pic, new)
                print("Renaming {0} to {1}".format(pic, new))
            else:
                print("Would be renaming {0} to {1}".format(pic, new))


user_description = input("What is the new prefix to the file? This is like"
                         "a general title:\n")

# prep the description so that it is in file name form
final_des = re.sub(" ", "_", user_description)
final_des += "_"
user_date = input("What is the date of the picture file? \n"
                  "Example: 20150518 or 201408\n")

doIt = input("Execute...Y/N?")
if doIt == "y" or doIt == "Y":
    pic_file_rename(final_des, user_date, execute=True)
else:
    pic_file_rename(final_des, user_date, execute=False)
