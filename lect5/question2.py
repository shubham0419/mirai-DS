# you have given a users.json , you have to insert a 
# product from products.json of id 5 in user cart whose id 5
import json
with open("lect5/data/users.json","r") as file:
  users = json.load(file)
  user = {}
  index = 0
  for x in users:
    if(x["id"] == 5):
      user = x
      index = users.index(x)
      break
  with open("lect5/data/products.json","r") as p:
    products = json.load(p)
    for x in products:
      if(x["id"] == 5):
        user["cart"].append(x)
        users[index] = user
        break
    with open("lect5/data/users.json","w") as u:
      json.dump(users,u)
