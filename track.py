import json 

followers = []
following = []

with open('followers.json', 'r') as file:
    
    reader = json.load(file)

    for i in reader:
        for entry in i["string_list_data"]:
            follower = entry.get("value")
            # print(entry.get("value"))

            followers.append(follower)

with open('following.json', 'r') as file: 
    
    reader = json.load(file)

    for i in reader:
        values = reader.get('relationships_following')
        
        for v in values:
            follow = v.get('string_list_data')
            
            for f in follow:
                following.append(f['value'])

for item in following:
    if item not in followers:
        print(item)
