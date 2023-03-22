current_users = ['khal', 'mah', 'lim', 'teteh', 'mas']
new_users = ['KHAL', 'kakak', 'mba','Teteh', 'mama']

current_users_lower = [users.lower() for users in current_users]

for users in new_users:
    if users.lower() in current_users_lower:
        print("'" + users + "'" + ' has already been used, you will need to enter a new username!\n')
    else:
        print("'" + users + "'" + ' has not been used, the username is available.\n')