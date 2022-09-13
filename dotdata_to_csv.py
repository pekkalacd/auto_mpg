# convert .data to .csv
import re
data={}
with open("auto-mpg.data","r") as infile:
    for i,line in enumerate(infile.readlines()):
        line=line.strip()
        line=line.replace('"','')
        p = r'\s+'
        line = re.split(p,line)
        line = line[:8] + [' '.join(line[8:])]
        data[i]=','.join(line)

with open("auto-mpg.csv","w") as outfile:
    outfile.write("index,mpg,cylinders,displacement,horsepower,weight,acceleration,model_year,origin,name\n")
    for i,line in data.items():
        outfile.write(f"{i},{line}\n")

print("done!")
