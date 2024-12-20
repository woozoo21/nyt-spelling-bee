import nltk
import requests
import json
from bs4 import BeautifulSoup

nltk.download('words')
from nltk.corpus import words
dictionary = set(words.words())
words = []

def brute(string, length, charset):
    global words
    if len(string) == length:
        return
    for char in charset:
        temp = string + char
        words.append(temp)
        brute(temp, length, charset)
    return words


def formatted(wordDict, middleLetter, dictionary, allLetters):
    final = {}
    listOfSizes = list(wordDict.keys())
    listOfSizes.sort(reverse=True)  # Sort by descending size (longest words first)
    largestWord = listOfSizes[0]
    
    # Start by checking for pangram (length of 7 letters or more)
    final["Pangram"] = []
    
    # Ensure all letters are used, accounting for repetitions of letters
    all_letters_set = set(allLetters)  # Unique set of letters to form a pangram
    
    # For words of length 7 or more, check if they are pangrams
    for word in wordDict.get(7, []):  # Assuming a pangram is at least 7 letters
        if middleLetter in word and word in dictionary:
            word_set = set(word)
            # A pangram must use each letter from the available letters set
            if all_letters_set <= word_set:  # Word should include all unique letters
                final["Pangram"].append(word)
    
    # Loop through the words starting from the longest
    for x in listOfSizes:
        if x >= 4:  # Minimum length 4
            final[str(x)] = []
            for word in wordDict[x]:
                if word in dictionary and middleLetter in word:
                    if word not in final[str(x)]:
                        final[str(x)].append(word)
    return final

def solver(middleLetter, otherLetters):
    global brute, words, formatted, dictionary
    middleLetter = str(middleLetter).lower()
    otherLetters = str(otherLetters).lower()
    otherLettersArray = list(otherLetters)
    allLetters = otherLettersArray + [middleLetter]  # All letters include the middle one
    words = []
    wordsSorted = {}

    # Get all possible words
    brute("", len(allLetters) + 1, "".join(allLetters))

    # Create arrays for dicts
    for word in words:
        wordsSorted[len(word)] = []

    # Append all the words
    for word in words:
        wordsSorted[len(word)].append(word)

    finalResult = formatted(wordsSorted, middleLetter, dictionary, allLetters)
    return finalResult

def solverRaw(middleLetter, otherLetters):
    global solver
    data = solver(middleLetter, otherLetters)
    data = list(data.values())
    merged_list = []
    for l in data:
        merged_list += l
    return merged_list

def webSolver():
    data = {}
    page = requests.get("https://www.nytimes.com/puzzles/spelling-bee")
    soup = BeautifulSoup(page.text, 'html.parser')
    answers = str(soup.find_all('script')[0]).replace('<script type="text/javascript">window.gameData = ', "").replace("</script>", "")
    parsed = json.loads(answers)

    # Normal answers
    answersList = list(parsed["today"]["answers"])
    answersList.sort(key=len, reverse=True)  # Sort longest first
    for answer in answersList:
        data[str(len(answer))] = []

    for answer in answersList:
        data[str(len(answer))].append(answer)

    return data