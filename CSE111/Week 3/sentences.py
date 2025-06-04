"""
Author: Noah Weston
Date: 10 Nov 2022
Assignment: 05 Prove Milestone: Testing and Fixing Functions
Purpose: Generate a random sentence. Intended to be tested by seperate program.
"""
import random

def main():
    """
    Quantity	Verb Tense
    1.	single	past
    2.	single	present
    3.	single	future
    4.	plural	past
    5.	plural	present
    6.	plural	future
    """
    nwSentenceNum = 1
    nwQuantity = 0
    nwTense = ""
    while nwSentenceNum < 7:
        if nwSentenceNum == 1:
            nwQuantity = 1
            nwTense = "past"

        elif nwSentenceNum == 2:
            nwQuantity = 1
            nwTense = "present"

        elif nwSentenceNum == 3:
            nwQuantity = 1
            nwTense = "future"

        elif nwSentenceNum == 4:
            nwQuantity = 2
            nwTense = "past"

        elif nwSentenceNum == 5:
            nwQuantity = 2
            nwTense = "present"

        else:
            nwQuantity = 2
            nwTense = "future"

        nwSentence = get_sentence(nwQuantity, nwTense)

        print(f"{nwSentence}.")
        
        nwSentenceNum += 1

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    elif tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    else:
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_preposition():
    """
    Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    word = random.choice(words)

    return word

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    nwPreposition = get_preposition()
    nwDeterminer = get_determiner(quantity)
    nwNoun = get_noun(quantity)
    nwPhrase = nwPreposition + " " + nwDeterminer + " " + nwNoun

    return nwPhrase

def get_sentence(quantity, tense):
    """
    Make a sentence using functions to get words.
    """
    nwDeterminer = get_determiner(quantity)
    nwNoun = get_noun(quantity)
    nwVerb = get_verb(quantity, tense)
    nwPhrase = get_prepositional_phrase(quantity)

    nwSentence = nwDeterminer.capitalize() + " " + nwNoun + " " + nwVerb + " " + nwPhrase

    return nwSentence

if __name__ == "__main__":
    main()