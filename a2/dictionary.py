thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict["brand"])
print(thisdict)
x = thisdict.keys()
print(x) #before the change
car["brand"] = "Jaguar"
print(x) #after the change
x = thisdict.values()

thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

for k,v in thisdict2.items():
  print(k)
  for items in v:
    print(items)
