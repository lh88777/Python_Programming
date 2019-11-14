f = open('IDay.txt', "r", encoding='utf-8')
file = f.read()
print(file)

#Removing special symbols
symbols = "!()-[];:'\,<>./?#*_’"
cleaned = ""
for g in file:
    if g not in symbols:
        cleaned = cleaned + g
print(cleaned)

# Removing lower case
text_final = cleaned.lower()
print(text_final)

#Count word while creating dictionary
def word_count(f):
    d = dict()
    for c in text_final.split(' '):
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dictionary = (word_count(text_final))
print(dictionary)
