def findMax(scores):
    max = -1
    for i in scores:
        if scores[i] > max and i[0] != i[1]:
            max = scores[i]
    return max

def main():
    wordDict = eval(open("Word_relations.txt", "r").read())
    wordCount = eval(open("Word_counts.txt", "r").read())
    scores = {}

    for i in wordDict:
        if i[0] in wordCount and i[1] in wordCount:
            scores[i] = wordDict[i] / wordCount[i[0]] / wordCount[i[1]]

    maxVal = findMax(scores)
    factor = 100 / maxVal
    for i in scores:
        scores[i] = scores[i] * factor

    finalScoreFile = open("Scores.txt", "w")
    finalScoreFile.write(str(scores))
    finalScoreFile.close()

if __name__ == "__main__":
    main()
