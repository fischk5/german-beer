# Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.s
import requests
import nltk
import random
from nltk import word_tokenize

tagDict = {}
adverb = []
noun = []
preposition = []
adjective = []
verb = []
coordinatingConjunction = []
determiner = []
cardinalDigit = []
existentialThere = []
foreignWord = []
adjectiveComparative = []
adjectiveSuperlative = []
listMarker = []
modal = []
nounPlural = []
nounProperSingular = []
nounProperPlural = []
predeterminer = []
possessive = []
personalPronoun = []
possessivePronoun = []
particle = []
to = []
uh = []
verbPast = []
verbGerund = []
verbPastParticiple = []
verbZ = []
whDeterminer = []
whPossessivePronoun = []
whAdverb = []

url = "http://www.gutenberg.org/files/5200/5200.txt"
script = requests.get(url)
script = script.text
sentenceStructures = []

tagDict["CC"] = coordinatingConjunction
tagDict["RB"] = adverb
tagDict["IN"] = preposition
tagDict["NN"] = noun
tagDict["JJ"] = adjective
tagDict["VBP"] = verb
tagDict["DT"] = determiner
tagDict["CD"] = cardinalDigit
tagDict["EX"] = existentialThere
tagDict["FW"] = foreignWord
tagDict["JJR"] = adjectiveComparative
tagDict["JJS"] = adjectiveSuperlative
tagDict["LS"] = listMarker
tagDict["MD"] = modal
tagDict["NNS"] = nounPlural
tagDict["NNP"] = nounProperSingular
tagDict["NNPS"] = nounProperPlural
tagDict["PDT"] = predeterminer
tagDict["POS"] = possessive
tagDict["PRP"] = personalPronoun
tagDict["PRP$"] = possessivePronoun
tagDict["RP"] = particle
tagDict["TO"] = to
tagDict["UH"] = uh
tagDict["VBD"] = verbPast
tagDict["VBG"] = verbGerund
tagDict["VBN"] = verbPastParticiple
tagDict["VBZ"] = verbZ
tagDict["WDT"] = whDeterminer
tagDict["WP$"] = whPossessivePronoun
tagDict["WRB"] = whAdverb

sentence = "Although Gregor wasn't able to hear any news directly he did listen to much of what was said in the next rooms, and whenever he heard anyone speaking he would scurry straight to the appropriate door and press his whole body against it.  There was seldom any conversation, especially at first, that was not about him in some way, even if only in secret.  For two whole days, all the talk at every mealtime was about what they should do now; but even between meals they spoke about the same subject as there were always at least two members of the family at home - nobody wanted to be at home by themselves and it was out of the question to leave the flat entirely empty.  And on the very first day the maid had fallen to her knees and begged Gregor's mother to let her go without delay.  It was not very clear how much she knew of what had happened but she left within a quarter of an hour, tearfully thanking Gregor's mother for her dismissal as if she had done her an enormous service."

def addLexicalValue(tagged, target):
    if tagged[1] == target and tagged[0] not in tagDict[target] and not tagged[0].isupper():
        tagDict[target].append(tagged[0].replace("'", ""))

def buildLibrary(input):
    tokens = word_tokenize(input)
    tags = nltk.pos_tag(tokens)
    for tag in tags:
        for key in tagDict:
            if tag[1] == key:
                addLexicalValue(tag, key)

def studySentenceStructures(input):
    tokens = word_tokenize(input)
    tags = nltk.pos_tag(tokens)
    structure = []
    index = 0
    while index < len(tags):
        if tags[index][0] != "." and tags[index][1] in tagDict:
            structure.append(tags[index][1])
        else:
            sentenceStructures.append(structure)
            structure = []
        index += 1

def genSentence(input):
    chosenStructure = random.choice(sentenceStructures)
    newSentence = ""
    index = 0
    while index < len(chosenStructure):
        tag = chosenStructure[index]
        word = random.choice(tagDict[tag])
        if index == 0:
            word = word.lower().capitalize()
            newSentence += word
        else:
            word = word.lower()
            newSentence += " " + word
        index += 1
    newSentence += "."
    print(newSentence)
    print("")

def addSentences(amount, source):
    for number in range(amount):
        genSentence(source)

buildLibrary(sentence)
studySentenceStructures(sentence)
addSentences(4, sentence)
