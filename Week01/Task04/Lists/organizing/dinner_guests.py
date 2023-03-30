invitation_list = ['marilyn monroe', 'Irfan Khan', 'GrandMother']

""" 
for person in invitation_list:
    print("Hello " + person.title() + "! You are invited to dinner.") """

print("I am inviting " + str(len(invitation_list)) + " people to dinner.")


print("Unfortunately, Marilyn Monroe can't make it to dinner.")

invitation_list[0] = 'Marcus Aurelius'

""" for person in invitation_list:
    print("Hello " + person.title() + "! You are invited to dinner.") """

print("I am inviting " + str(len(invitation_list)) + " people to dinner.")


print("-----------We have found a bigger table!-------------")

invitation_list.insert(0, 'Nelson Mandela')
invitation_list.insert(2, 'Albert Einstein')
invitation_list.append('Mahatma Gandhi')

""" for person in invitation_list:
    print("Hello " + person.title() + "! You are invited to dinner.") """


print("I am inviting " + str(len(invitation_list)) + " people to dinner.")

print("-----------We can only invite two people for dinner.-------------")
print("I'm sorry to inform you all that my new dinner table won't arrive in time for the dinner. I can invite only two people for dinner.\n")

 #while len(invitation_list) > 2:
 #   print("I'm sorry to inform you " + invitation_list.pop().title() + " that you are not invited to dinner.")

#for person in invitation_list:
#    print("Hello " + person.title() + " you are still invited to dinner.")

print("I am inviting " + str(len(invitation_list)) + " people to dinner.")

del invitation_list[0] # This is the same as invitation_list.pop(0)
del invitation_list[0] 

print(invitation_list)


