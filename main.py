from characters.characters import characters
from urllib.request import Request, urlopen
from os import makedirs, path
from time import sleep

# for page in range(1, 50):
# r = requests.get(URL)
# chars.extend(r.json())

# write answers to file

# How many characters names start with "A"?
# How many characters names start with "Z"?
def name_starts_with(char):
    with open('name_starts_with_%s.txt' % char, 'w') as f:
        count = 0
        for character in characters:
            if character["name"][0] == char:
                f.write(character["name"] + "\n")
                count += 1
        f.write(str(count))

# How many characters are dead?
def dead_characters():
    with open("dead_characters.txt", 'w') as f:
        count = 0
        for character in characters:
            if character["died"] != '':
                f.write(character['died'] + '\n')
                count += 1
        f.write(str(count))

# Who has the most titles?
def most_titles():
    with open("most_titles.txt", 'w') as f:
        title_count = 0
        title_winner = ''
        for character in characters:
            if len(character['titles']) > title_count:
                title_count = len(character['titles'])
                title_winner = character['name']
        f.write('%s, %d' % (title_winner, title_count))

# How many are Valyrian?
def valyrian_count():
    with open('valyrian_count.txt', 'w') as f:
        count = 0
        for character in characters:
            if character['culture'] == 'Valyrian':
                f.write(character['name'] + '\n')
                count += 1
        f.write(str(count))

# What actor plays "Hot Pie"?
def who_is_hot_pie():
    with open('who_is_hot_pie.txt', 'w') as f:
        for character in characters:
            if 'Hot Pie' in character['name']:
                for actor in character['playedBy']:
                    f.write(actor + '\n')


# How many characters are *not* in the tv show?
def characters_not_in_show():
    with open('characters_not_in_show.txt', 'w') as f:
        count = 0
        for character in characters:
            if len(character['tvSeries']) == 1 and character['tvSeries'][0] == '':
                f.write(character['name'] + '\n')
                count += 1
        f.write(str(count))

# Produce a list of characters with the last name "Targaryen"
def last_name_targaryen():
    with open('last_name_targaryen.txt', 'w') as f:
        for character in characters:
            if 'Targaryen' in character['name']:
                f.write(character['name'] + '\n')

# Create a histogram of the house (it's the "allegiances" key)
def houses_histogram():
    with open('houses_histogram.txt', 'w') as f:
        houses = {}
        for character in characters:
            for allegiance in character['allegiances']:
                allegiance = get_house_from(allegiance)
                if allegiance not in houses:
                    houses[allegiance] = 1
                else:
                    houses[allegiance] += 1
        for allegiance, count in houses.items():
            f.write("%s: %d\n" % (allegiance, count))

def make_houses_package():
    # get string of houses dictionary from api
    # write string to file as .py
    if not path.exists('houses'):
        makedirs('houses')
    with open('houses/houses.py', 'w+') as f:
        f.write('houses = ')
        i = 1
        while True:
            req = Request("https://www.anapioficeandfire.com/api/houses?page=%d&pageSize=100" % i, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read().decode('utf-8')
            if webpage == '[]':
                f.write(']')
                break
            # keep incrementing until page is empty
            else:
                if i != 1:
                    f.write(',')
                else:
                    f.write('[')
                webpage = webpage[1:-1] # remove first and last char which is [ and ]
                f.write(webpage)
                i += 1
    with open('houses/__init__.py', 'w') as f:
        f.write('')

def get_house_from(allegiance):
    if not path.exists('houses'):
        make_houses_package()
    from houses.houses import houses
    for house in houses:
        if allegiance == house['url']:
            return house['name']

# How many characters names start with "A"?
name_starts_with("A")
# How many characters names start with "Z"?
name_starts_with("Z")
# How many characters are dead?
dead_characters()
# Who has the most titles?
most_titles()
# How many are Valyrian?
valyrian_count()
# What actor plays "Hot Pie"?
who_is_hot_pie()
# How many characters are *not* in the tv show?
characters_not_in_show()
# Produce a list of characters with the last name "Targaryen"
last_name_targaryen()
# Create a histogram of the house (it's the "allegiances" key)
houses_histogram()