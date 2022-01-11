import json

folderName = "Folder Name"
folderId = None

with open("bitwarden_export.json", "r") as file:
    jsonData = json.load(file)
  

for i in jsonData["folders"]:
    if i.get("name") == folderName:
        folderId = i.get("id")
        break
    
if folderId == None:
    exit(1)
       
resultItems = []
for i in jsonData["items"]:
    if i.get("folderId") == folderId:
        resultItems.append(i)

jsonData["items"] = resultItems

with open("FolderSpecificPasswords.json", "w+") as outfile:
    json.dump(jsonData, outfile, indent=4)