from pathlib import Path
import time
stupidWords = ["the", "of", "and", "a", "to", "in", "is", "you", "that", "it", "was", "for", "on", "are", "as", "with", "his", "they", "i", "at", "be", "this", "have", "from", "or", "one", "had", "by", "word", "but", "not", "what", "all", "were", "we", "when", "your", "there", "use", "an", "each", "which", "she", "do", "how", "their", "if", "will", "up", "other", "about", "out", "many", "then", "them", "some", "her", "would", "make", "like", "him", "into", "has", "can", "said", "these", "so"]

def cleanFile(file):
    str = file.read_text(encoding='ISO8859-1')
    str = "Cloud load balancing is a type of load balancing that is performed in cloud computing"
    str = str.lower()
    
    for i in stupidWords:
        str = str.replace(" " + i + " ", " ")
    return str

def main():
    cleanDirFile = open("Stupid_words_removed.txt", 'r')
    cleanDirs = cleanDirFile.readlines()
    cleanDirs = [i[:len(i) - 1] for i in cleanDirs]
    cleanDirFile = open("Stupid_words_removed.txt", 'a')
    count = 0
    bypassedMax = False
    for child in Path(r'C:\Users\CWHar\Downloads\Coding\Personal\Codenames\merged_articles').iterdir():
        encodedFile = str(str(child).encode('utf-8'))
        curTime = time.time()
        if encodedFile not in cleanDirs:
            if not bypassedMax:
                print(count, "directories bypassed")
                bypassedMax = True
                temp = cleanFile(child)
                file = open(child, 'w')
                
                file.write(temp)
                file.close()

            print("Directory cleaned", time.time() - curTime)
            cleanDirFile.write(encodedFile + '\n')
            cleanDirFile.close()
            cleanDirFile = open("Stupid_words_removed.txt", 'a')
        else:
            count += 1
    pass

if __name__ == "__main__":
    main()
