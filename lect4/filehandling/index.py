
with open("lect4/filehandling/dist/myfile.txt","w") as file:
  file.write("this is line 1")
  file.writelines(["\nthis is line 1","\nthis is line 2","\nthis is line 3"])

try :
  with open("lect4/filehandling/dist/myfile.txt","x") as file:
    file.write("this is line 1")
except FileExistsError:
  print("file alredy exist")


with open("lect4/filehandling/dist/myfile.txt","r") as file:
  data = file.read()
  print(data)


with open("lect4/filehandling/dist/myfile.txt","r") as file:
  data = file.readlines()
  print(data)

with open("lect4/filehandling/dist/myfile.txt","a") as file:
  file.write("this is line 4")

# delete operations
import os
filepath = "lect4/filehandling/myfile.txt"
# file delete
if(os.path.exists(filepath)):
  os.remove(filepath)
else:
  print("file not exists")

folderpath = "lect4/filehandling/dummy"
if(os.path.exists(folderpath)):
  os.rmdir(folderpath)              #rmdir -> remove directory(folder)
  print("folder deleted")
else:
  print("folder not exists")

# json data
import json

with open("lect4/filehandling/dist/data.json","w") as file:
  students = [
    {
      'name':"dummy name",
      'roll no':2345,
      "class":"section A",
      "batch":"CS",
      "year":1
    }
  ]
  json.dump(students,file,indent=2)
  print("json data inserted")


with open("lect4/filehandling/dist/data.json","r") as file:
  data = json.load(file)
  print(data)
  print(data[0])
  data.append(
    {
      'name':"my name",
      'roll no':2344,
      "class":"section A",
      "batch":"CS",
      "year":1
    }
  )
  with open("lect4/filehandling/dist/data.json","w") as file:
    json.dump(data,file,indent=2)

# Q add a new object in the student array in the file
# read file ,load json , insert new object in students
# write in data.json, json.dump(students)

