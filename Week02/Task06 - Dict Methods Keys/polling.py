favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

should_poll = ['jen', 'sarah', 'edward', 'phil', 'john', 'jane']

for name in should_poll:
    if name in favorite_languages.keys():
        print(f"Thank you for taking the poll, {name.title()}!")
    else:
        print(f"{name.title()}, please take our poll!")