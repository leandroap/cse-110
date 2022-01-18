# File: 02-Prove_WordGames_LAP.py
# Author: Leandro Amaral Pereira

vowel_list = ("a","e","i","o","u")

print("Please enter the following:\n")

#Asking the required questions
adjective = input("adjective: ").lower()
animal = input("animal: ").lower()
verb_one = input("verb: ").lower()
exclamation = input("exclamation: ").capitalize()
verb_two = input("verb: ").lower()
#I changed the question to be possible understand that is a different one
anotherverb = input("another verb: ").lower()

#Asking additional questions
friend_name = input("a friend name: ").capitalize()
object_name = input("an object: ").lower()
fruit = input("a fruit: ").lower()

if object_name.startswith(vowel_list):
    object_sentence = f"an {object_name}"
else:
    object_sentence = f"a {object_name}"

if fruit.startswith(vowel_list):
    fruit_sentence = f"an {fruit}"
else:
    fruit_sentence = f"a {fruit}"

#Here I'm formatting the story with the answers
story = f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb_one} down the hallway. "{exclamation}!" I yelled. But all I could think to do was to {verb_two} over and over. Miraculously, that caused it to stop, but not before it tried to {anotherverb} right in front of my family.'

#Here I'm formatting the additional story with the answers
additional_story = f" Later I met my friend {friend_name} to talk about this crazy story, then we decided to buy {object_sentence}, and eat {fruit_sentence}."

print("\nYour story is:\n")

print(story + additional_story)