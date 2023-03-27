# 3-6. More Guests:  "You just found a bigger dinner table, so now more space is available. 
Think of three more guests to invite to dinner."

guest_list = ['Albert Einstein', 'Isaac Newton', 'Stephen Hawking']

print(f"{guest_list[0]} is invited to dinner.")
print(f"{guest_list[1]} is invited to dinner.")
print(f"{guest_list[2]} can't make it to dinner.")

guest_list.insert(0, 'Galileo Galilei')
guest_list.insert(3, 'Max Planck')
guest_list.append('Neil deGrasse Tyson')

print(f"\n{guest_list[0]} is invited to dinner.")
print(f"{guest_list[1]} is invited to dinner.")
print(f"{guest_list[2]} is invited to dinner.")
print(f"{guest_list[3]} is invited to dinner.")
print(f"{guest_list[5]} is invited to dinner.")