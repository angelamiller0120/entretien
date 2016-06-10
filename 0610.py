import requests
url = "http://opendata.paris.fr/explore/dataset/subventions-accordees-et-refusees/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true"
r = requests.get(url)
with open("data.csv","wb") as code:
    code.write(r.content)

import pandas as pd
import numpy as np
data=pd.read_csv("data.csv")
