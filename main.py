from characters.characters import characters

# write answers to file

# How many characters names start with "A"?
# How many characters names start with "Z"?
def name_starts_with(char):
    with open('name_starts_with_%s.txt' % char, 'w') as f:
        for character in characters:
            if character[0] == char:
                f.write(character)

# How many characters are dead?
def dead_characters():
    pass

# Who has the most titles?
def most_titles():
    pass

# How many are Valyrian?
def valyrian_count():
    pass

# What actor plays "Hot Pie"?
def who_is_hot_pie():
    pass

# How many characters are *not* in the tv show?
def characters_not_in_show():
    pass

# Produce a list of characters with the last name "Targaryen"
def last_name_targaryen():
    pass

# Create a histogram of the house (it's the "allegiances" key)
def houses_histogram():
    pass


name_starts_with("A")