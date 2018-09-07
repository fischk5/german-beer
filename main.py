# Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
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
# huckleberryRaw = open('huckleberry.txt').read()

tagDict["CC"] = coordinatingConjunction
tagDict["RB"] = adverb
tagDict["IN"] = preposition
tagDict["NN"] = noun
tagDict["JJ"] = adjective
tagDict["VBP"] = verb
tagDict["DT"] = determiner

sentence = "Pretty soon a spider went crawling up my shoulder, and I flipped it off and it lit in the candle; and before I could budge it was all shriveled up.  I didn't need anybody to tell me that that was an awful bad sign and would fetch me some bad luck, so I was scared and most shook the clothes off of me. I got up and turned around in my tracks three times and crossed my breast every time; and then I tied up a little lock of my hair with a thread to keep witches away.  But I hadn't no confidence.  You do that when you've lost a horseshoe that you've found, instead of nailing it up over the door, but I hadn't ever heard anybody say it was any way to keep off bad luck when you'd killed a spider."

def addLexicalValue(tagged, target):
    if tagged[1] == target and tagged[0] not in tagDict[target]:
        tagDict[target].append(tagged[0])

def buildLibrary(input):
    tokens = word_tokenize(sentence)
    tags = nltk.pos_tag(tokens)
    for tag in tags:
        addLexicalValue(tag, 'CC')
        addLexicalValue(tag, 'RB')
        addLexicalValue(tag, 'IN')
        addLexicalValue(tag, 'NN')
        addLexicalValue(tag, 'JJ')
        addLexicalValue(tag, 'VBP')
        addLexicalValue(tag, 'DT')

buildLibrary(sentence)

print(adverb)
print(noun)
print(preposition)
print(adjective)
print(verb)
print(coordinatingConjunction)
