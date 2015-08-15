#!/usr/bin/python3
#
# this is not working since it is for some reason copying the old name and appeding
# the new one
from fileNameChanger import FileNameChanger
import os

# get the directory where the files are located
directory = input("Directory?   --->   ")
obj = FileNameChanger(directory)
print("\nContents of {}.".format(obj.directory))
print()
print(obj.dir_content())
print()

# get the new common name for the files.
description = input("What is the new common name for these files? Ex. "
                    " Beautiful Sunny Day.\n:")
obj.set_description(description)

# get the search date
search = input("The date to search for? Remember this can be as long as it "
               "needs to be.\n:")
obj.set_search_date(search)

# preview the changes
print("PREVIEW>>>>>>>\n")
obj.rename_file(execute=False)
print()

# continue?
execute = input("Would you like to continue with the rename?\nY/N?: ")
if(execute == 'Y' or execute == 'y'):
    obj.rename_file(execute=True)
else:
    print("Well thanks for wasting my time. lol Just joking, I'm just a "
          "program")



