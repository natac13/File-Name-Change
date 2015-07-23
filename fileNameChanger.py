import os
import re


class FileNameChanger():
    """Convert name of files from android phone to readable format.

    @var directory
    @var directory_path
    @var final_description

    @method set_description
    """

    directory_path = "/home/natac/"

    def __init__(self, directory):
        """Sets directory and directory_path variables.

        directory - name of directory where files which need to be changed
        exist. This will be capitalized inside the class since users trends
        to not remember.
        """
        self.directory = directory.capitalize()
        self.directory_path += self.directory
        os.chdir(self.directory_path)

    def get_dir(self):
        return self.directory

    def set_description(self, description):
        """Sets a new common title for the files.

        @param Description - string input which may have spaces and acts as
        the common name for files
        """
        if(description):
            self.final_description = re.sub(" ", "_", description)
            self.final_description += "_"
        else:
            self.final_description = "natac_{0}_".format(self.directory)

    def set_search_date(self, date):
        """Will set the date to use to search the directory.

        @param date - should be an string of numbers which are from user input
        """

        if(not isinstance(date, str)):
            date = str(date)

        self.search_date = date

    def rename_file(self, execute=False):
        """Will search in the given directory for files that start with the
    given date which can be any length, maybe year and month or could include
    the day.

    description - A title like name for the group of photo files that are to
    be labeled together.

    search - The date that will be used to first find the files and then use
    it in the renaming process

    execute - A boolean to preview the changes.

    new - modified pic name with index added as well as the last 8 characters,
    which represent the date the photo was taken.

    """

        index = 1
        new = ""

        for media in os.listdir(self.directory_path):
            if media.startswith(self.search_date):
                new += self.final_description
                new += media[:8] + "_"
                new += str(index)
                new += media[-4:]
                index += 1
                if execute:
                    os.rename(media, new)
                    print("Renaming {0} to {1}".format(media, new))
                else:
                    print("Would be renaming {0} to {1}".format(media, new))
            else:
                print("There are no files in {0} to match {1}".format(
                      self.directory_path, self.search_date))
