"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random

def getWords():
    nounsOpen = open("nouns.txt", 'r').read()
    verbsOpen = open("verbs.txt", 'r').read()
    articlesOpen = open("articles.txt", 'r').read()
    prepositionsOpen = open("prepositions.txt", 'r').read()

    nouns = nounsOpen.split()
    verbs = verbsOpen.split()
    articles = articlesOpen.split()
    prepositions = prepositionsOpen.split()

    return tuple(nouns), tuple(verbs), tuple(articles), tuple(prepositions)

def sentence(nouns, verbs, articles, prepositions):
    """Builds and returns a sentence."""
    return nounPhrase(articles, nouns) + " " + verbPhrase(articles, nouns, verbs, prepositions)

def nounPhrase(articles, nouns):
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase(articles, nouns, verbs, prepositions):
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase(articles, nouns) + " " + \
           prepositionalPhrase(articles, nouns,prepositions)

def prepositionalPhrase(articles, nouns, prepositions):
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase(articles, nouns)

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))

    nouns, verbs, articles, prepositions = getWords()

    for count in range(number):
        print(sentence(nouns, verbs, articles, prepositions))

# The entry point for program execution
if __name__ == "__main__":
    main()

