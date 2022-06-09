import pandas as pd
import requests
import numpy as np
import pylab as plt


csv = pd.read_csv("/users/dgreen/Downloads/sianctapi-selected-observations-629f614f1b157.csv")
for id in csv["Sequence ID"]:
    if id[0] == "d":
        try:
            for number in range(len(id)):
                url = f"http://ids.si.edu/ids/deliveryService?id=emammal_image_{id}i{number}&max=1000"
                ret = requests.get(url)
                if ret.ok:
                    content = ret.content
                    file_handle = open(f"/Users/dgreen/Docs/coyote_images/{id}_{number}.png","wb")
                    file_handle.write(content)
                    file_handle.close()
                    print(f"The image {url} was successfully saved.")
        except:
            print(f"The URL {url} does not work.")
print("Done")