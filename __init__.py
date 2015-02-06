import os
directory, filename = os.path.split(__file__)
data = os.path.join(directory, 'ingredients-list')

with open(data, 'r') as f:
    known_ingredients = []
    for line in f:
        known_ingredients.append(line.strip())

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
def remove_punctuation(s):
    s_sans_punct = ""
    for letter in s:
        if letter not in punctuation:
            s_sans_punct += letter
    return s_sans_punct


def parse(label):
    """Identify the known ingredients in the supplied product label"""
    found = []
    words = map(lambda x: remove_punctuation(x.strip()),
                label.lower().replace('and', ',').split(','))
    for word in words:
        possible = []
        for ing in known_ingredients:
            if ing in word:
                possible.append(ing)
        if possible:
            found.append(max(possible, key=len))
    return sorted([i for i in set(found)])
