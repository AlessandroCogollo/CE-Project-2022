import os
import shutil
import time


def get_file_or_folder_age(path):
    # getting ctime of the file/folder
    # time will be in seconds
    ctime = os.stat(path).st_ctime
    # returning the time
    return ctime


def remove_folder(path):
    # removing the folder
    if not shutil.rmtree(path):
        # success message
        print(f"{path} is removed")
    else:
        # failure message
        print(f"Unable to delete the {path}")


def remove_file(filepath):
    # removing the file
    if not os.remove(filepath):
        # success message
        print(f"{filepath} is removed successfully")
    else:
        # failure message
        print(f"Unable to delete the {filepath}")


class GarbageCleaner:

    def __init__(self):
        self.path = "../flaskr/templates/plots"
        self.hours = 12

    def main(self):

        print("---- starting cleanup ----")
        # converting hours to seconds
        # time.time() returns current time in seconds
        seconds = time.time() - (self.hours * 60 * 60)

        if os.path.exists(self.path):
            for root_folder, folders, files in os.walk(self.path):
                if seconds >= get_file_or_folder_age(root_folder):
                    # removing the folder
                    remove_folder(root_folder)
                    break
                else:
                    # checking folder from the root_folder
                    for folder in folders:
                        folder_path = os.path.join(root_folder, folder)
                        # comparing with the days
                        if seconds >= get_file_or_folder_age(folder_path):
                            # invoking the remove_folder function
                            remove_folder(folder_path)
                    # checking the current directory files
                    for file in files:
                        file_path = os.path.join(root_folder, file)
                        # comparing the days
                        if seconds >= get_file_or_folder_age(file_path):
                            # invoking the remove_file function
                            remove_file(file_path)
            else:
                # if the path is not a directory
                # comparing with the days
                if seconds >= get_file_or_folder_age(self.path):
                    # invoking the file
                    remove_file(self.path)
        else:

            # file/folder is not found
            print(f'"{self.path}" is not found')
