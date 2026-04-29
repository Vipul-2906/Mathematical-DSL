class Token:
    def __init__(self, token_type, value, line):
        self.type = token_type
        self.value = value
        self.line = line

    def __repr__(self):
        return f"{self.type}({self.value}) at line {self.line}"


class Lexer:
    KEYWORDS = {"solve", "where", "find"}
    OPERATORS = {"="}
    VALID_SYMBOLS = {","}

    def __init__(self, text):
        self.text = text

    def tokenize(self):
        tokens = []
        lines = self.text.split("\n")

        for line_number, line in enumerate(lines, start=1):
            words = line.replace(",", " , ").split()

            for word in words:

                if word in self.KEYWORDS:
                    tokens.append(Token("KEYWORD", word, line_number))

                elif word in self.OPERATORS:
                    tokens.append(Token("OPERATOR", word, line_number))

                elif word in self.VALID_SYMBOLS:
                    tokens.append(Token("COMMA", word, line_number))

                elif word.isdigit():
                    tokens.append(Token("NUMBER", int(word), line_number))

                elif word.isidentifier():
                    tokens.append(Token("IDENTIFIER", word, line_number))

                else:
                    raise Exception(
                        f"Lexical Error: Invalid token '{word}' at line {line_number}"
                    )

        return tokens