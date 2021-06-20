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
