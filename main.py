import sys
from tokens import *


KEYWORDS = [
    "int", "float", "str", "if", "else", "for", "while", "endif", "endwhile", "endfor"
]
ALPHABETS = "QWERTYUIOPASDFGHJKLXCVBNMqwertyuiopasdfghjklxcvbnm"
NUMS = "1234567890"
SYMBOLS = "!@#$%^&*()_+=-`~;\"'{[]}<>,./?:\\|"

def main():
    if len(sys.argv) > 1: fileName = sys.argv[1]
    else: fileName = "p.jh51"

    with open(fileName, "r") as myfile: code = myfile.read()

    codeLines = separateLines(code)

    for line in codeLines:
        tokens = tokenizeLine(line)
        for token in tokens: print(token.type, token.value)

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
        i += 1
    return tokens

if __name__ == "__main__":
    main()
