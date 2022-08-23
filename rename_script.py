import shutil
import os
import os.path
from os.path import isfile, join

##### FOR MASS RENAMING IMAGES CAPTURED TO READABLE STRINGS#####
def main():
    

    folder = "F:\\Videos\\Ghost in the Shell SAC\\Season 1"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"Episode - {str(count + 1)}.mkv"
        # foldername/filename, if .py file is outside folder
        src = f"{folder}/{filename}"
        dst = f"{folder}/{dst}"

        # rename() function will
        # rename all the files
        # os.rename(src, dst) does not work on Windows OS!
        newFileName=shutil.move(src, dst)

        print ("The renamed file has the name:",newFileName)


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
