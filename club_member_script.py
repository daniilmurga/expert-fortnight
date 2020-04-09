# THIS CODE IS TO EXTRACT People's ID's who are already member of the trading club
import datetime
import json
from archive_bot.db import check_club
from archive_bot.db import init_db

now = datetime.datetime.now()

#FUNCTION CHECK_CLUB checks that user has completed all of the registration
completed_register_members = check_club()

#Extracting ALL Id's that completed register
members_list = []
for i in range(len(completed_register_members)):
    members_list.append(completed_register_members[i][1])

#Leaving only unique Id's
def unique_members(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

#Creating file with these Id's
name_of_the_file = 'club_file_{}_{}.txt'.format(now.date(), now.time())
list_to_write = unique_members(members_list)
with open(name_of_the_file, 'w') as f:
    f.write(json.dumps(list_to_write))

#Now read the file back into a Python list object
#with open('test.txt', 'r') as f:
#    a = json.loads(f.read())

print('file_created')
print("file_name is")
print(name_of_the_file)




