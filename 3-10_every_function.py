# 3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

languages = ['English', 'Russian', 'Hebrew', 'French', 'Italian', 'Japanese', 'Arabic']

languages.append("German")
languages.insert(8, "Spanish")
languages.pop()
languages.remove("French")
languages.sort()
sorted(languages)
languages.reverse()
print(languages)