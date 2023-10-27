import random
import os

# Task 1 ------------------------------


def gcd(a, b):
    while not a == b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


num1 = 42
num = 30

# print("The GCD of", num1,"and", num,"is", gcd(num1, num))

# Task 2 -------------------------------


def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

# num = int(input("Enter a number: "))
# if isEven(num):
#     print(num, "is even")
# else:
#     print(num, "is odd")

# Task 3 -------------------------------


def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"

# loop through numbes 1 to 100 inclusive and print the result of fizzBuzz
# for i in range(1, 101):
#     print(fizzBuzz(i))


# Task 4 -------------------------------


# estimating pi using the monte carlo method. Check if a random point is inside a circle of radius 1/2 inside a square of side 1. The 'precision' variable is the number of decimal places to which pi is estimated.


# def estimatPi(precision):
#     inside = 0
#     total = 0
#     for i in range(10**precision):
#         if i % 100000 == 0:
#             print(i, 10 ** precision)
#         x = random.random()
#         y = random.random()
#         if (x**2 + y**2)**0.5 < 0.5:
#             inside += 1
#         total += 1
#     return 16 * (inside / total)


# print(estimatPi(7))


# Task 5 -------------------------------

# Backtracking Caesar Cipher decryption algorithm. Create a txt document called "english_words" that are filled with english words, each on a new line, no punctation. The example is "computerscienceisveryfun", shifted once. Puncation and spaces are not allowed. If the algorithm does not work, check if the words are in the english_words document. The algorithm may not get exactly the right decryption in this scenario: the phrase is made up words which have words inside of the them. For example, "another" would be shown as "an", "not"", "her". To fix this problem, I would need to add a check to see if the word is a substring of another word in the english_words document. This would be very slow for long pieces of text, so I have not done it.

# Want to show the process a bit better? Set to True!
fullVerobse = False


def decryptText(cipherText):
    possibleDecryptions = []
    def load_words():
        # open english_words.txt and return a set of words
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'english_words')
        with open(file_path) as word_file:
            valid_words = set(word_file.read().split())
        return valid_words
    english_words = load_words()

    def checkForIndexToBacktrackTo(indexesToBackTrackTo):
        if not indexesToBackTrackTo:
            return False
        for index in indexesToBackTrackTo:
            if index[1] or index[1] == None:
                return True
        return False

    def findIndexToBacktrackTo(indexesToBackTrackTo, setToFalse):
        for i in range(len(indexesToBackTrackTo) - 1, -1, -1):
            if indexesToBackTrackTo[i][1]:
                if setToFalse:
                    indexesToBackTrackTo[i][1] = False
                return indexesToBackTrackTo[i][0]
            elif indexesToBackTrackTo[i][1] == None:
                indexesToBackTrackTo[i][1] = True
                return indexesToBackTrackTo[i][0]
        return None

    # add the index inputted to indexesToBackTrackTo with a True value
    def addIndexToBacktrackTo(indexesToBackTrackTo, index):
        indexesToBackTrackTo.append([index, True])
        return indexesToBackTrackTo

    for caesarShift in range(26):
        shiftedText = []
        for char in cipherText:
            if char.islower():
                shiftedText.append(
                    chr((ord(char) - ord('a') + caesarShift) % 26 + ord('a')))
            elif char.isupper():
                shiftedText.append(
                    chr((ord(char) - ord('A') + caesarShift) % 26 + ord('A')))
            else:
                shiftedText.append(char)

        currentIndex = 0
        currentWordBeingDecoded = ""
        backtracking = False

        currentDecodedArrayOfWords = []
        indexesToBackTrackTo = [[0, None]]

        justBacktracked = False

        print("Shift:", caesarShift,
              "--------------------------------------------------------")

        while checkForIndexToBacktrackTo(indexesToBackTrackTo):
            if not backtracking:

                if not justBacktracked:
                    currentIndex = findIndexToBacktrackTo(
                        indexesToBackTrackTo, False)

                if fullVerobse:
                    print("Current Index: (not backtracking)", currentIndex)

                currentWordBeingDecoded += shiftedText[currentIndex]

                while currentWordBeingDecoded.lower() not in english_words:
                    if fullVerobse:
                        print("Current Word:", currentWordBeingDecoded)
                    else:
                        if len(currentDecodedArrayOfWords) == 0:
                            print(currentWordBeingDecoded)
                        else:
                            print(" ".join(currentDecodedArrayOfWords) +
                                  f" {currentWordBeingDecoded}")
                    currentIndex += 1

                    if currentIndex >= len(shiftedText):
                        if len(currentDecodedArrayOfWords) == 0:
                            print(
                                "-----No possible decryption for this caesar shift-----")
                            indexesToBackTrackTo = []
                            break

                        if fullVerobse:
                            print("We need to backtrack...")
                        # end of string reached, need to backtrack
                        backtracking = True
                        break
                    else:
                        currentWordBeingDecoded += shiftedText[currentIndex]
                else:
                    # currentWordBeingDecoded is now a word
                    if fullVerobse:
                        print(currentWordBeingDecoded, " is a word")
                    currentIndex += 1

                    if currentIndex >= len(shiftedText):
                        possibleDecryptions.append(
                            " ".join(currentDecodedArrayOfWords + [currentWordBeingDecoded]))
                        if not fullVerobse:
                            print(" ".join(currentDecodedArrayOfWords +
                                           [currentWordBeingDecoded]))
                        print("Possible Decryption Found:",
                              " ".join(possibleDecryptions))
                        indexesToBackTrackTo = []
                        break

                    currentDecodedArrayOfWords.append(currentWordBeingDecoded)
                    indexesToBackTrackTo = addIndexToBacktrackTo(
                        indexesToBackTrackTo, currentIndex)
                    currentWordBeingDecoded = ""
            else:
                if fullVerobse:
                    print("Current Index: (backtracking)", currentIndex)
                backtracking = False
                currentIndex = findIndexToBacktrackTo(
                    indexesToBackTrackTo, True)
                currentWordBeingDecoded = currentDecodedArrayOfWords.pop()
                justBacktracked = True

    if len(possibleDecryptions) == 0:
        # print("No possible decryptions")
        return False

    # loop through all possible decryptions
    # for i in range(len(possibleDecryptions)):

    return possibleDecryptions


# Example usage
cipherText = "dpnqvufstdjfodfjtwfszgvo"
decryptedText = decryptText(cipherText)

print("")
print("-------------------------Decryptions-------------------------")

if not decryptedText:
    print("No possible decryptions")
    exit()

for i in range(len(decryptedText)):
    print(f"Possible Decryption {i+1}:", decryptedText[i])

print("Decrypted Text:", " ".join(decryptedText))
