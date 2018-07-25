# Lets play question and response
import random

response1 = 'I am well'
response2 = 'Lets eat dinner twice'
response3 = 'I have a sore foot'
response4 = 'Inside.  Somewhere.  Alone.'
response5 = 'Its about time you asked me about that'
response6 = 'Probably check your pocket.'
response7 = 'Yes'
response8 = 'As far as I can tell, it is cold.'

responses = [response1, response2, response3, response4, response5, response6, response7, response8]

question = input("####\n")

while question != 'exit':
    responseInt=random.randint(0,len(responses))
    print(responses[responseInt])
    question = input("####\n")
print(response)
