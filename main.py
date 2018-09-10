# Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.s
import requests
import nltk
import random
from nltk import word_tokenize

tagDict = {}
adverb = [] # describes a verb, adjective, or another adverb
noun = [] # person place, thing, or idea
preposition = [] # a word governing, and usually preceding, a noun or pronoun and expressing a relation to another word or element in the clause, as in “the man on the platform,” “she arrived after dinner,”
adjective = [] # describes a noun or pronoun
verb = [] # An action
coordinatingConjunction = [] # join two main clauses to make a complete sentence
determiner = [] # determines the kind of reference a noun or noun group has, for example a, the, every
cardinalDigit = [] # number
existentialThere = [] #  a clause that refers to the existence or presence of something. Examples in English include the sentences "There is a God" and "There are boys in the yard".
foreignWord = [] # Foreign word
adjectiveComparative = [] # They are used in sentences where two nouns are compared
adjectiveSuperlative = [] # A superlative adjective compares three or more nouns
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
verbBase = []
verbPast = []
verbGerund = []
verbPastParticiple = []
verbZ = []
whDeterminer = []
whPossessivePronoun = []
whPronoun = []
whAdverb = []

url = "https://www.gutenberg.org/files/1342/1342-0.txt"
script = requests.get(url)
script = script.text
script = script.replace("'", "")
script = script.replace(",", "")
script = script.replace("-", "")
script = script.replace(";", ".")
script = script.replace(":", "")
script = script.replace("_", "")
sentenceStructures = []

exStructure = [["DT", "JJ", "NN", "VBD"], ["DT", "NN", "VBD"]]

tagDict["CC"] = coordinatingConjunction
tagDict["RB"] = adverb
tagDict["VB"] = verbBase
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
tagDict["WP"] = whPronoun
tagDict["WRB"] = whAdverb

sentence = "Although Gregor wasn't able to hear any news directly he did listen to much of what was said in the next rooms, and whenever he heard anyone speaking he would scurry straight to the appropriate door and press his whole body against it.  There was seldom any conversation, especially at first, that was not about him in some way, even if only in secret.  For two whole days, all the talk at every mealtime was about what they should do now; but even between meals they spoke about the same subject as there were always at least two members of the family at home - nobody wanted to be at home by themselves and it was out of the question to leave the flat entirely empty.  And on the very first day the maid had fallen to her knees and begged Gregor's mother to let her go without delay.  It was not very clear how much she knew of what had happened but she left within a quarter of an hour, tearfully thanking Gregor's mother for her dismissal as if she had done her an enormous service."

sentence = sentence.replace("'", "")
sentence = sentence.replace(",", "")
sentence = sentence.replace("-", "")
sentence = sentence.replace(";", ".")
sentence = sentence.replace(":", "")

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

def genSentenceFromStructure(input):
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

def addSentencesFromStructure(amount, source):
    for number in range(amount):
        genSentenceFromStructure(source)

def genSentenceNoStructure(input):
    structure = random.choice(exStructure)
    #structure = exStructure[1]
    index = 0
    newSentence = ""
    while index < len(structure):
        tag = structure[index]
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

def addSentencesNoStructure(amount, source):
    for number in range(amount):
        genSentenceNoStructure(source)

buildLibrary(script)
studySentenceStructures(script)
addSentencesFromStructure(25, script)
#addSentencesNoStructure(15, script)

## TODO: Capture groups of words together instead of individual words and buildLibrary
## structures based off that instead
