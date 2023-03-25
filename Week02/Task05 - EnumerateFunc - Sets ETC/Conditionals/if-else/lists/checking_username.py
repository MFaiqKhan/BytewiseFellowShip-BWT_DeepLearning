current_users = ['faiq', 'khan', 'usman', 'ali', 'ahmed']

new_users = ['faiq', 'khan', 'usman', 'ali', 'ahmed', 'zain', 'zohaib']

for new_user in new_users:
    if new_user in current_users:
        print("Sorry, " + new_user + " is already taken. Please enter a new username.")
    else:
        print("Great, " + new_user + " is available.")