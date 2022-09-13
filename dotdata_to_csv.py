import re
import pandas as pd
import numpy as np

# read in the data from auto-mpg.data found via https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/
# & parse into csv delimiter repr
data=[]
with open("auto-mpg.data","r") as infile:
    for line in infile.readlines():
        line=line.strip()
        line=line.replace('"','')
        p = r'\s+'
        line = re.split(p,line)
        line = line[:8] + [' '.join(line[8:])]
        data.append(','.join(line))

# write out auto-mpg.csv
with open("auto-mpg.csv","w") as outfile:
    outfile.write("mpg,cylinders,displacement,horsepower,weight,acceleration,model_year,origin,car_name\n")
    for line in data:
        outfile.write(f"{line}\n")


# read in as df
df = pd.read_csv("auto-mpg.csv")

# replace all '?' with np.nan
df.replace('?',np.nan,inplace=True)

# according to index via https://archive.ics.uci.edu/ml/datasets/Auto+MPG,
# horsepower is continous convert dtypes to float64 and car_name is str [will be type('O') in pandas]
df['horsepower']=df['horsepower'].astype(np.float64)
df['car_name']=df['car_name'].astype(str)

# if pass, this line will execute; write df to auto_mpg.csv
df.to_csv('auto_mpg.csv',index=None)

print("done!")
