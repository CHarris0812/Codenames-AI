from pathlib import Path
import time
codenamesWords = open("Codenames_words.txt", "r").readlines()
codenamesWords = [i[:-1] for i in codenamesWords]

#Ice cream, new york, loch ness, scuba diver
#have multiple words
def readFile(file):
    wordCounts = {}
    wordRelations = {}
    str = file.read_text(encoding='ISO8859-1')
    str = str.upper()
    str = str.replace("ICE CREAM", "ICECREAM")
    str = str.replace("NEW YORK", "NEWYORK")
    str = str.replace("LOCH NESS", "LOCHNESS")
    str = str.replace("SCUBA DIVER", "SCUBADIVER")
    words = str.split(" ")

    for i in range(len(words)):
        if words[i] in wordCounts:
            wordCounts[words[i]] += 1
        else:
            wordCounts[words[i]] = 1

        if words[i] in codenamesWords:
            for j in range(max(0, i - 5), min(len(words), i + 5)):
                if (words[i], words[j]) in wordRelations:
                    wordRelations[(words[i], words[j])] += 11 - abs(i - j)
                else:
                    wordRelations[(words[i], words[j])] = 11 - abs(i - j)

                if words[j] in codenamesWords:
                    if (words[j], words[i]) in wordRelations:
                        wordRelations[(words[j], words[i])] += 11 - abs(i - j)
                    else:
                        wordRelations[(words[j], words[i])] = 11 - abs(i - j)
    return wordCounts, wordRelations

def combineDicts(dict1, dict2):
    #for i in dict2:
    #    if i in dict1:
    #        dict1[i] += dict2[i]
    #    else:
    #        dict1[i] = dict2[i]
    #return dict1
    return dict1 | dict2

def clean(dictionary, count):
    newDict = {}
    for i in dictionary:
        if dictionary[i] > count:
            newDict[i] = dictionary[i]
    return newDict

def main():
    readDirFile = open("Read_directories.txt", 'r')
    readDirs = readDirFile.readlines()
    readDirs = [i[:len(i) - 1] for i in readDirs]
    readDirFile = open("Read_directories.txt", 'a')
    count = 0
    dirList = []
    bypassedMax = False
    timeUntilReset = 2
    tempTime = time.time()
    wordCounts = {}
    wordRelations = {}
    for folder in Path(r'C:\Users\CWHar\Downloads\Coding\Personal\Codenames\articles').iterdir():

        encodedFile = str(str(folder).encode('utf-8'))
        wordCounts = {}
        wordRelations = {}
        if encodedFile not in readDirs:
            

            curTime = time.time()
            if not bypassedMax:
                print(count, "directories bypassed")
                bypassedMax = True
            for child in Path(folder).iterdir():
                if child.is_file():
                    newWordCounts, newWordRelations = readFile(child)
                    wordCounts = combineDicts(wordCounts, newWordCounts)
                    wordRelations = combineDicts(wordRelations, newWordRelations)

            print("Directory read", time.time() - curTime)
            dirList.append(encodedFile) 
        else:
            count += 1
    pass

if __name__ == "__main__":
    main()
