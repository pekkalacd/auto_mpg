# convert .data to .csv
import re
data=[]
with open("auto-mpg.data","r") as infile:
    for i,line in enumerate(infile.readlines()):
        line=line.strip()
        line=line.replace('"','')
        p = r'\s+'
        line = re.split(p,line)
        line = line[:8] + [' '.join(line[8:])]
        data.append(','.join(line))

with open("auto-mpg.csv","w") as outfile:
    outfile.write("mpg,cylinders,displacement,horsepower,weight,acceleration,model_year,origin,name\n")
    for line in data:
        outfile.write(f"{line}\n")

print("done!")
