import pandas as pd
import urllib.request

def url_to_jpg(i, url, file_path):
    try:
        '''
            -- i : number of image.
            -- url : a URL address of a given image.
            -- file_path : where to save the final image. 
        '''


        filename = 'image-{}.jpg'.format(i)
        full_path = '{}{}'.format(file_path, filename)
        urllib.request.urlretrieve(url, full_path)
    
        print('{} saved.'.format(filename))

        return None
    except:
        print("The URL " + url + " does not work." )

FILENAME = 'imagedownloads.csv'
FILE_PATH = '/Users/dgreen/Pictures/RECONN/black_bear'

urls = pd.read_csv(FILENAME)

for i, url, in enumerate(urls.values):
    url_to_jpg(i, url[0], FILE_PATH)

print("Download complete.")