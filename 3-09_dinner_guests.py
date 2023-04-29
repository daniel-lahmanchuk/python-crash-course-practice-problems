# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 42), use len() to print a message indicating the number of people you're inviting to dinner.

# 3-4. Guest List:
guest_list = ['Albert Einstein', 'Isaac Newton', 'Stephen Hawking']

print("Number of people attending: " + str(len(guest_list)))

# 3-5. Changing Guest List:
guest_list = ['Albert Einstein', 'Isaac Newton', 'Stephen Hawking']

guest_list.remove('Stephen Hawking')
guest_list.append('Neil deGrasse Tyson')

print("Number of people attending: " + str(len(guest_list)))

# 3-6. More Guests:
guest_list = ['Albert Einstein', 'Isaac Newton']

guest_list.insert(0, 'Galileo Galilei')
guest_list.insert(3, 'Max Planck')
guest_list.append('Neil deGrasse Tyson')

print("Number of people attending: " + str(len(guest_list)))

# 3-7. Shrinking Guest List:
guest_list = ['Albert Einstein', 'Isaac Newton', 'Stephen Hawking']

removed_guest = guest_list.remove('Stephen Hawking')

print("Number of people attending: " + str(len(guest_list)))