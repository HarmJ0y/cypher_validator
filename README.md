# cypher_validator
Simple Python valuidator for Cypher query syntax.

Install the Python ANTLR library with `antlr4-python3-runtime==4.9.2` (reflected in requirements.txt).

You can then run `python cypher_validator.py`

## Notes

ANTLR was downloaded with `curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar`, the BloodHound Cypher grammar file was downloaded with `curl -O https://raw.githubusercontent.com/SpecterOps/BloodHound/main/packages/go/cypher/grammar/Cypher.g4`, and the Python lexer/parser files were generated with `java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 Cypher.g4`
