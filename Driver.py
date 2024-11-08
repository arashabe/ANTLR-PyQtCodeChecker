#Driver.py
import sys
from antlr4 import *
from generated.LanguageLexer import LanguageLexer
from generated.LanguageParser import LanguageParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LanguageParser(stream)
    tree = parser.start_()
    print("Parsing completato senza errori.")

if __name__ == '__main__':
    main(sys.argv)
