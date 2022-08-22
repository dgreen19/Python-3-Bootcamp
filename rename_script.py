##### FOR MASS RENAMING IMAGES CAPTURED TO READABLE STRINGS#####
def main():

    folder = "/Users/dgreen/Docs/rename_test"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"Ursus americanus_{filename}"
        # foldername/filename, if .py file is outside folder
        src = f"{folder}/{filename}"
        dst = f"{folder}/{dst}"

        # rename() function will
        # rename all the files
        os.rename(src, dst)


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
