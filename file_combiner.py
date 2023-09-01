from pathlib import Path
import time
import os.path
import re
pattern = re.compile('[^a-z ]', re.I)

save_path = r"C:\Users\CWHar\Downloads\Coding\Personal\Codenames\merged_articles"
def main():
    #for file in directory:
    #mergeFile()
    mergeDirFile = open("Merged_directories.txt", 'r')
    mergeDirs = mergeDirFile.readlines()
    mergeDirs = [i[:len(i) - 1] for i in mergeDirs]
    mergeDirFile = open("Merged_directories.txt", 'a')
    count = 0
    bypassedMax = False
    for folder in Path(r'articles').iterdir():
        merged = ""
        encodedFile = str(str(folder).encode('utf-8'))
        curTime = time.time()
        if encodedFile not in mergeDirs:
            if not bypassedMax:
                print(count, "directories bypassed")
                bypassedMax = True

            count = 0
            for child in Path(folder).iterdir():
                count += 1
                if count % 100 == 0:
                    folderName = str(str(folder).encode("utf-8"))
                    folderName = re.sub(pattern, '', folderName)
                    folderName = folderName[9:] + str(count)
                    fileName = os.path.join(save_path, folderName + ".txt")
                    fileName = Path(fileName)
                    file = open(Path(fileName), "w")
                    file.write(merged)
                    file.close()
                    merged = ""



                if child.is_file():
                    merged += " "
                    merged += child.read_text(encoding='ISO8859-1')

            
            print("Directory Merged", time.time() - curTime)
            mergeDirFile.write(encodedFile + '\n')
            mergeDirFile.close()
            mergeDirFile = open("Merged_directories.txt", 'a')
        else:
            count += 1
    pass

if __name__ == "__main__":
    main()