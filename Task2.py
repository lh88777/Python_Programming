#Importing file into Python
f = open('IDay.txt', "r", encoding='utf-8')
if f.mode == 'r':
    IDay = f.read()

#Removing punctuations from string
punctions = "!()-[];:'\,<>./?@#$%^&*_~’"
cleaned = ""
for char in IDay:
    if char not in punctions:
        cleaned = cleaned + char

#Lower case
lowerc = ""
for char in cleaned:
    if cleaned.islower() == False:
        lowerc = cleaned.lower()

    #if char in cleaned.islower():
        #lowerc = cleaned.lower() + char

#dict: key - word; value - amount

#counting words
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

dictionary = ( word_count(lowerc))
print(dictionary)