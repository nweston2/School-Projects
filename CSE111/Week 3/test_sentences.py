"""
Author: Noah Weston
Date: 10 Nov 2022
"""
import sentences
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = sentences.get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = sentences.get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    """
    Verify the function get_noun works
    """
    nwSingleNouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    nwPluralNouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    #test single nouns
    for _ in range(4):
        nwWord = sentences.get_noun(1)
        assert nwWord in nwSingleNouns

    #test plural nouns
    for _ in range(4):
        nwWord = sentences.get_noun(2)
        assert nwWord in nwPluralNouns

def test_get_verb():
    """
    Verify the function get_verb works
    """
    nwFutureVerbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    nwPastVerbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    nwPresentSingular = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    nwPresentPlural = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    #test future
    for _ in range(4):
        nwWord = sentences.get_verb(1, "future")
        assert nwWord in nwFutureVerbs

    #test past
    for _ in range(4):
        nwWord = sentences.get_verb(1, "past")
        assert nwWord in nwPastVerbs

    #test present singular
    for _ in range(4):
        nwWord = sentences.get_verb(1, "present")
        assert nwWord in nwPresentSingular

    #test present plural
    for _ in range(4):
        nwWord = sentences.get_verb(2, "present")
        assert nwWord in nwPresentPlural

def test_get_sentence():
    """
    Make sure sentences are correctly generated
    """
    #lists of verbs
    nwVerbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write", 
        "drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote",
        "drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes", 
        "drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    #lists of nouns
    nwNouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    #lists of determiners
    nwDeterminers = ["a", "one", "the", "some", "many", "the"]

    #lists of prepositions
    nwPrepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(4):
        nwSentence = sentences.get_sentence(1, "past")
        nwWords = nwSentence.split(" ")

        assert nwWords[0].lower() in nwDeterminers
        assert nwWords[1] in nwNouns
        assert nwWords[2] in nwVerbs
        assert nwWords[3] in nwPrepositions
        assert nwWords[4] in nwDeterminers
        assert nwWords[5] in nwNouns

    for _ in range(4):
        nwSentence = sentences.get_sentence(1, "future")
        nwWords = nwSentence.split(" ")

        assert nwWords[0].lower() in nwDeterminers
        assert nwWords[1] in nwNouns
        assert nwWords[4] in nwPrepositions
        assert nwWords[5] in nwDeterminers
        assert nwWords[6] in nwNouns

    for _ in range(4):
        nwSentence = sentences.get_sentence(1, "present")
        nwWords = nwSentence.split(" ")

        assert nwWords[0].lower() in nwDeterminers
        assert nwWords[1] in nwNouns
        assert nwWords[2] in nwVerbs
        assert nwWords[3] in nwPrepositions
        assert nwWords[4] in nwDeterminers
        assert nwWords[5] in nwNouns

    for _ in range(4):
        nwSentence = sentences.get_sentence(2, "present")
        nwWords = nwSentence.split(" ")

        assert nwWords[0].lower() in nwDeterminers
        assert nwWords[1] in nwNouns
        assert nwWords[2] in nwVerbs
        assert nwWords[3] in nwPrepositions
        assert nwWords[4] in nwDeterminers
        assert nwWords[5] in nwNouns

def test_get_preposition():
    """"
    Ensures the function get_preposition() works
    """

    nwPrepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(4):
        nwPreposition = sentences.get_preposition()

        assert nwPreposition in nwPrepositions

def test_get_prepositional_phrase():
    """
    Ensures the function get_prepositional_phrase() works
    """
    nwPrepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    nwDeterminers = ["a", "one", "the", "some", "many", "the"]

    nwNouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman", 
        "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):
        nwPhrase = sentences.get_prepositional_phrase(1)
        nwWords = nwPhrase.split(" ")

        assert nwWords[0] in nwPrepositions
        assert nwWords[1] in nwDeterminers
        assert nwWords[2] in nwNouns

    for _ in range(4):
        nwPhrase = sentences.get_prepositional_phrase(2)
        nwWords = nwPhrase.split(" ")

        assert nwWords[0] in nwPrepositions
        assert nwWords[1] in nwDeterminers
        assert nwWords[2] in nwNouns

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])