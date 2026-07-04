import sys
from tokens import *
from at89c51 import *

KEYWORDS = ["int", "float", "str", "if", "else", "for", "while", "endif", "endwhile", "endfor", "free"]
ALPHABETS = "QWERTYUIOPASDFGHJKLXCVBNMqwertyuiopasdfghjklxcvbnm"
NUMS = "1234567890"
SYMBOLS = "!@#$%^&*()_+=-`~;\"'{[]}<>,./?:\\|"

assemblyCode = ""

def main():
    if len(sys.argv) > 1: fileName = sys.argv[1]
    else: fileName = "p.jh51"

    with open(fileName, "r") as myfile: code = myfile.read()

    codeLines = separateLines(code)

    tokenizedLines = []
    for line in codeLines:
        tokens = tokenizeLine(line)
        tokenizedLines.append(tokens)

    interpretTokenizedLines(tokenizedLines)

def interpretTokenizedLines(tokenizedLines: list[list[Token]]):
    for tokenizedLine in tokenizedLines:
        if not tokenizedLine: continue
        
        for i, token in enumerate(tokenizedLine):
            if token.type == TokenType.KEYWORD:
                if token.value == "int":
                    j = i + 1

                    while j < len(tokenizedLine):
                        currentToken = tokenizedLine[j]
                        if currentToken.type == TokenType.IDENTIFIER:
                            addr = getUnallocatedAddr()
                            allocateAddr(addr)
                            variableTracker[Variable(currentToken.value)] = addr
                        j += 1

                elif token.value == "free":
                    j = i + 1
                    while j < len(tokenizedLine):
                        currentToken = tokenizedLine[j]
                        if currentToken.type == TokenType.IDENTIFIER:
                            toDelete = []
                            for variable, addr in variableTracker.items():
                                if variable.name == currentToken.value: toDelete.append(variable)
                            for variable in toDelete:
                                freeAddr(variableTracker[variable]) 
                                del variableTracker[variable]
                        j += 1

    print(RAMtracker, "\n")
    print(variableTracker)


def separateLines(code: str) -> list[str]:
    separated = []
    lastIndex = 0
    insideString = False

    for i, character in enumerate(code):
        currentLine = code[lastIndex + 1: i].lstrip()
        if character == "\"": insideString = not insideString
        elif character == "\n" and not insideString and currentLine: separated.append(currentLine); lastIndex = i
    separated.append(code[lastIndex + 1: ].lstrip())
    return separated

def tokenizeLine(line: str) -> list[Token]:
    line += " "
    tokens = []
    i = 0
    j = 0
    lineLength = len(line)

    while i < lineLength:
        character = line[i]
        currentCharacter = ""

        if character in ALPHABETS:
            j = i
            while line[j] in ALPHABETS or line[j] in NUMS:
                currentCharacter += line[j]
                j += 1
            i = j - 1
            if currentCharacter in KEYWORDS:
                tokens.append(
                    Token(
                        TokenType.KEYWORD, currentCharacter
                    )
                )
            else:
                tokens.append(
                    Token(
                        TokenType.IDENTIFIER, currentCharacter
                    )
                )

        elif character in NUMS:
            j = i
            while line[j] in NUMS:
                currentCharacter += line[j]
                j += 1
            i = j - 1
            tokens.append(
                Token(
                    TokenType.INTEGER, currentCharacter
                )
            )

        elif character in SYMBOLS:
            if character == "+": 
                tokens.append(
                    Token(
                        TokenType.OPERATOR, character
                    )
                )
            elif character == "-":
                tokens.append(
                    Token(
                        TokenType.OPERATOR, character
                    )
                )
            elif character == "*":
                tokens.append(
                    Token(
                        TokenType.OPERATOR, character
                    )
                )
            elif character == "/":
                tokens.append(
                    Token(
                        TokenType.OPERATOR, character
                    )
                )
            elif character == "(":
                tokens.append(
                    Token(
                        TokenType.OPERATOR, character
                    )
                )
            elif character == ")":
                tokens.append(
                    Token(
                        TokenType.OPERATOR, character
                    )
                )
            elif character == "=":
                tokens.append(
                    Token(
                        TokenType.OPERATOR, character
                    )
                )
            elif character == ",":
                tokens.append(
                    Token(
                        TokenType.OPERATOR, character
                    )
                )
            
        i += 1
    return tokens

def addCodeLines(*lines):
    global assemblyCode
    for line in lines: assemblyCode += line

if __name__ == "__main__":
    main()
