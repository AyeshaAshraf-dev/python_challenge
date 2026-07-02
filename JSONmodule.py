import json 


people_string = '''
{
    "people": [
        {
            "name": "John Sena",
            "phone": "2323-33-2",
            "emails": ["johnsena322@gmail.com", "johnsmith232@gmail.com"],
            "has_license": false
        },
        {
            "name": "brokyin",
            "phone": "9753233-2",
            "emails": ["broklitin322@gmail.com", "broklyin322@gmail.com"],
            "has_license": true
        }
    ]
}
'''


data = json.loads(people_string)
# print(type(data))#dict
for person in data['people']:
    # print(person['name'])
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

#how to load JSON files nto poython objects and thhen write those obj back to json 

with open('jsonmodule2.json') as f:
    data = json.load(f)

for state in data['states']:
    del state['abbreviation']
#dump method converts the data to a json file
#dump s method converts the data to json string

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)

list = data.get('list',{}).get('resourses',[])
print(len(list))







# for more understanting


# Sample data: Notice Bob doesn't have a phone key!
users = [
    {"name": "Alice", "phone": "123-456"},
    {"name": "Bob"} 
]

# APPROACH 1: Using square brackets (CRASHES)
for user in users:
    print(user['phone'])  # ERROR! Crashes when it hits Bob because 'phone' is missing.

# APPROACH 2: Using .get() (SAFE)
for user in users:
    # If 'phone' is missing, it gently defaults to "No Phone Provided"
    user_phone = user.get('phone', "No Phone Provided")
    print(f"{user['name']}: {user_phone}")

