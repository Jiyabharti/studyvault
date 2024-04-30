

                                #LISTS

# pop() removes the last thing from the list

# Guest list, if i could invite anyone to dinner, make a list
print('Who is your guest list?')
guest_list = ['austin butler', 'timothee chalemet', 'Leonardo di caprio', 'Florence Pugh']

# Oh no, she cant make it
# Have to remove her now
guest_list.remove('Florence Pugh')
print(guest_list)

# Someone else is coming now
guest_list.append('Zendaya')
print(guest_list)

# I need to replace Leonardo, he said his friend will come instead
# we have to refer to the values
# remember it NEVER STARTS with 1, it STARTS WITH 0
guest_list[2] = 'Jared Leto'
print(guest_list)

# Can also delete a value
del guest_list[2]
print(guest_list)


# EXERCISE - add one guest to the beginning using insert
# add one guest to the middle using insert
# add one guest to the end using append

guest_list.insert(0,'Bill Starzgard', )
print(guest_list)


guest_list.insert(2,'Jiya Bharti', )
print(guest_list)

guest_list.append('Ryan Gosling')
print(guest_list)

# .pop() - removes last item in a list


# sort lists
jiya_friends = ['arya', 'tom', 'joel', 'hanzla', 'anoop', 'misha']
jiya_friends.sort()
print(jiya_friends)

# it sorts lists into alphabetical order


# -----You can also reverse sort it-----

jiya_friends.sort(reverse=True)
print(jiya_friends)



