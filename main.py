# Devon Taylor
# U4L2
# DS
# 12/9/24

from StackClass import ArrayStack

def read(inPath):
  with open (inPath, 'r') as openFile:
    contents = openFile.readlines()
    return contents

def write(outPath, contents):
  with open(outPath, 'w') as openFile:
    openFile.write(contents)

def clean(contents):
  cleanCont = []
  for word in contents:
    cleanWord = ""
    for letter in word:
      if ord(letter) > 32 and ord(letter) < 65 or ord(letter) > 90 and ord(letter) < 97 or ord(letter) > 122:
        continue
      else:
        cleanWord += letter

    cleanCont.insert(0, cleanWord)
  return cleanCont

def main():
    stack = ArrayStack()
    inPath = "earnest.txt"
    outPath = "flipped.txt"

    contents = read(inPath)
    cleanCont = clean(contents)

    flippedCont = ""
    contList = []

    for i in cleanCont:
      sentence = i.split()
      for i in range(len(sentence)):
        flippedCont += sentence[-1]
        flippedCont += " "
        del sentence[-1]
      flippedCont += "\n"
      contList.append(flippedCont)
      flippedCont = ""

    for i in range(len(contList)):
      stack.push(contList[-1])
      del contList[-1]

    for i in range(len(stack)):
      flippedCont += stack.pop()

    write(outPath, flippedCont)

if __name__ == "__main__":
    main()