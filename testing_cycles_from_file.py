import json

#Reading txt as JSON is working okay
with open('club_file_2020-04-07_13:32:55.615214.txt', 'r') as f:
    list_with_user_id = json.loads(f.read())

for i in range(len(list_with_user_id)):
    print('this user will get an image', list_with_user_id[i])
