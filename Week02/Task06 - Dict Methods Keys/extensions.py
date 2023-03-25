users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

users['aurelius'] = { 'first': 'emperor', 'last': 'aurelius', 'location': 'rome' }
users['aurelius']['last'] = 'antoninus'

for username, user_info in users.items():
    print(f"Username: {username}")
    print(f"\tFull name: {user_info['first'].title()} {user_info['last'].title()}")
    print(f"\tLocation: {user_info['location'].title()}")