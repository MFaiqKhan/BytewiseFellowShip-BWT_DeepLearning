invitation_list = ['marilyn monroe', 'Irfan Khan', 'GrandMother']

for person in invitation_list:
    print("Hello " + person.title() + "! You are invited to dinner.")

print("Unfortunately, Marilyn Monroe can't make it to dinner.")

invitation_list[0] = 'Marcus Aurelius'

for person in invitation_list:
    print("Hello " + person.title() + "! You are invited to dinner.")


