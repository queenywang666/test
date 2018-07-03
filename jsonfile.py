import json
data={"id":[],"path":[]}
img_path="imglist.txt"#your img path list
with open(img_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        lable=line.split("/")[1].split(".")[0].split("-")
        r=lable[0]+"-"+lable[1]
        data["id"].append(r)
        data["path"].append(line)
json = json.dumps(data,sort_keys=True, indent=2)
fileObject = open('jsonFile.json', 'w')
fileObject.write(json)
fileObject.close()
# print json
