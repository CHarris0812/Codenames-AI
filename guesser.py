def evaluate(words, scores, clue):
    relevantDict = {}
    for i in words:
        if (i, clue) in scores:
            relevantDict[(i, clue)] = scores[(i, clue)]
        else:
            relevantDict[(i, clue)] = 0

    order = {k: v for k, v in sorted(relevantDict.items(), key=lambda item: round(item[1], 6))}
    return order

def main():
    scores = eval(open("Scores.txt", "r").read())
    words = input("Input words capitalized and separated by spaces").split(" ")
    
    while True:
        clue = input("what is the clue")
        wordOrder = evaluate(words, scores, clue)
        print(wordOrder)
        removed = input("what words were removed").split(" ")
        tempRemoved = input("what words did the other team remove").split(" ")
        removed = removed + tempRemoved
        for i in removed:
            if i in words:
                words.remove(i)

if __name__ == "__main__":
    main()