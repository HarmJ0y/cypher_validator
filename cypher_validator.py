import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from CypherLexer import CypherLexer
from CypherParser import CypherParser


class CypherErrorListener(ErrorListener):
    def __init__(self):
        super(CypherErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"line {line}:{column} {msg}")

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return self.errors

def validate_query(query):
    input_stream = InputStream(query)
    lexer = CypherLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CypherParser(stream)
    error_listener = CypherErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    try:
        parser.oC_Cypher()
        if error_listener.has_errors():
            print("Cypher query is invalid:")
            for error in error_listener.get_errors():
                print(error)
        else:
            print("Cypher query is valid.")
    except Exception as e:
        print(f"Cypher query is invalid: {e}")

if __name__ == "__main__":
    query = """
...example query...
"""
    validate_query(query)
