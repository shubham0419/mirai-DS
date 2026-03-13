

d = {
  "a":"hello",
  "b":1,
  "c":[1,5,7,["2D"],True]
}

print(d["c"][3])

dd = {
  "a":"one",
  "b":{
    "a":1,
    "b":{
      "c":[5,7,9]
    }
  },
}

print(dd["b"]["b"]["c"][2])

# adding new key value pair
dd["c"] = "added key"
print(dd)

dd["b"]["b"]["c"].append(12)
print(dd)

dd["b"] = "overwritten key"
print(dd)

# dd.pop("c")
# print(dd)

# dd.popitem()
# print(dd)

for key in dd:
  print(key,"--->",dd[key])

for k,v in dd.items():
  print(k,"---->",v)

print(dd.items())    #-> converts dictonary in array of tupels 
# dict_items([ ('a', 'one'), ('c', 'added key') ])
