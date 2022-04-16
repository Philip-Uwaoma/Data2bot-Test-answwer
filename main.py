#A genertic program that:
#- Reads a JSON file similar to what's present in this location (./data/)
#- Sniffs the schema of the JSON file 
#- Dumps the output in (./schema/)


import json

# Opening JSON file
filename1 = input("what is the name of the file to be read? ")
try:
    openfile = open(filename1, "r")
except:
    print ("couldn't open file")
#with open(".\data_1.json", 'r') as openfile:

	# Reading from json file
json_object = json.load(openfile)
for key in json_object:
    if key == 'message':
        k = json_object[key]
#print(k)

#Function to link an item to its schema.
        
def Schema(item, Type):
        schema = {
            "type": Type,
            "tag": "",
            "description": "",
            "required": False}
        
        return schema
#Function to analyse the elements of a list
def Alist(list):
    sol = dict()
    for item in list:
        if type(item) is dict:
            sol.update(CreateDict(item))
        elif type(item) is str:
            Type = "str"
            sol[item] = Schema(item, Type)
    return sol

#Function to analyse the elements of the "message" element in a dictionary.
def CreateDict(message):
    Type = ""    
    solution = dict()
    for key in message:
        if type(message[key]) is dict:
            Type = "array"
            solution.update(CreateDict(message[key]))
        elif type(message[key]) is str:
            Type = "str"
        elif type(message[key]) is int:
            Type = "int"
        elif type(message[key]) is list:
            Type = "enum"
            temp = message[key]
            solution.update(Alist(temp))
            
        solution[key] = Schema(key, Type)
        
    return solution

C = CreateDict(k)
#print(C)

json_object = json.dumps(C, indent = 4)
  
# Writing to schema.json
filename = input("what is the name of the output file? ")
try:
    with open(filename, "w") as outfile:
        outfile.write(json_object)
except:
    print ("couldn't open file")

print("Done. Please open output file to view the schema.")
