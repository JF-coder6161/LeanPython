import json

filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("Please input username !")
    with open(filename, 'w') as username_json_obj:
        json.dump(username, username_json_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("welcome back, " + username + "!")
