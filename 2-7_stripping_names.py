# 2-7. Stripping Names: Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.

name = "     Daniel     "

print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())