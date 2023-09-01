import re
from pathlib import Path
import time
pattern = re.compile('[^a-z ]', re.I)
pattern2 = re.compile(" *")

def cleanFile(file):
    str = file.read_text(encoding='ISO8859-1')
    str = re.sub(pattern, '', str)
    str = str.replace("  ", " ")
    str = str.replace("  ", " ")
    return str

def main():
    #for file in directory:
    #CleanFile()
    cleanDirFile = open("Cleaned_directories.txt", 'r')
    cleanDirs = cleanDirFile.readlines()
    cleanDirs = [i[:len(i) - 1] for i in cleanDirs]
    cleanDirFile = open("Cleaned_directories.txt", 'a')
    count = 0
    bypassedMax = False
    for folder in Path(r'C:\Users\CWHar\Downloads\Coding\Personal\Codenames\articles').iterdir():
        encodedFile = str(str(folder).encode('utf-8'))
        curTime = time.time()
        if encodedFile not in cleanDirs:
            if not bypassedMax:
                print(count, "directories bypassed")
                bypassedMax = True
            for child in Path(folder).iterdir():
                if child.is_file():
                    temp = cleanFile(child)
                    file = open(child, 'w')
                
                    file.write(temp)
                    file.close()

            print("Directory cleaned", time.time() - curTime)
            cleanDirFile.write(encodedFile + '\n')
            cleanDirFile.close()
            cleanDirFile = open("Cleaned_directories.txt", 'a')
        else:
            count += 1
    pass

if __name__ == "__main__":
    main()