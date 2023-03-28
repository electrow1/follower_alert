import json  

      
# Data to be written  

dictionary ={
}  

      
# Serializing json   
with open("followers.json", "w") as outfile: 

    json.dump(dictionary, outfile)
