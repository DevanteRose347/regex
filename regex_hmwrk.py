import re
### In-Class Exercise #3 <br>
# Print each persons name and twitter handle, using groups, should look like:
# <p>==============<br>
#    Full Name / Twitter<br>
#    ==============</p>
# Derek Hawkins / @derekhawkins

#  Erik Sven-Osterberg / @sverik

#  Ryan Butz / @ryanbutz

#  Example Exampleson / @example

#  Ripal Pael / @ripalp

#  Darth Vader / @darthvader# 

# with open("names.txt") as f:
#     data = f.readlines()
#     print(data[0])
with open("names.txt") as f:
    first_data = f.readlines()
    print(first_data)

# ([a-z]\w+@\w+\.com) (.[0-9]{3}. [0-9]{3}-[0-9]{4}) ([A-Z]\w+,) ([A-Z]\w+) ([A-Z]\w+) (@[a-z]\w+)
 #([A-Z]\w+)? ([A-Z]\w+.)?
pattern = re.compile('([A-Z]\w+),\s([A-Z]\w+).*\s(@\w+)')
#([A-Z][a-z]+), ([A-Za-z-]*)([A-Z][a-z]+).*\s(@[a-zA-Z0-9]+)
# pattern = re.compile('[A-Z][a-z]+(\s[A-Z][a-z]*)?\s[A-Z][a-z]+')

for first_name in first_data:
    first_match = pattern.match(first_name)
    if first_match:
        print(first_match.group(2), first_match.group(1), " / ",first_match.group(3))
    else:
        print(None)

### Regex project

# Use python to read the file regex_test.txt 
# and print the last name on each line using regular expressions
# and groups (return None for names with no first and last name, or names 
# that aren't properly capitalized)
##### Hint: use with open() and readlines()
with open("regex_test.txt") as f:
    data = f.readlines()
    print(data)


pattern = re.compile('([A-Z]\w+)(\s[A-Z]\w*)?(\s[A-Z]\w+)')
# pattern = re.compile('[A-Z][a-z]+(\s[A-Z][a-z]*)?\s[A-Z][a-z]+')

for name in data:
    match = pattern.match(name)
    if match:
        print(match.group(0))
    else:
        print(None)




"""
Expected Output
Abraham Lincoln
Andrew P Garfield
Connor Milliken
Jordan Alexander Williams
None
None
"""