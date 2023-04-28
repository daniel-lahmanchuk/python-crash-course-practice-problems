# 3-7. Shrinking Guest List: You just found out that your new dinner table won't arrive in time for the dinner, and you have space for only two people for dinner.

guest_list = ['Albert Einstein', 'Isaac Newton', 'Stephen Hawking']

print("The table can only fit two people at dinner.")

removed_guest = guest_list.pop(2)

print(f"I'm sorry but {removed_guest} won't be able to make it to dinner.")
print(f"{guest_list[0]} will still be making it to dinner.")
print(f"{guest_list[1]} will still be making it to dinner.")
