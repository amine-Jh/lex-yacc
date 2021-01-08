import ply.lex as lex
import ply.yacc as yacc
 
 # List of token names.   This is always required


tokens = (
    '3ADAD',
    'PLUS',
    'NA9IS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUAL',
    'NAME',
    'FOR'
    )
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',

 }
tokens+=tuple(reserved.values())
 # Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_NA9IS   = r'\-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_FOR     =r'minajl'
t_IF      = r'ida'
t_NAME    = r"[a-zA-Z][a-zA-Z0-9_]*"
t_EQUAL=r'\='

 
 # A regular expression rule with some action code
def t_3ADAD(t):
     r'\d+'
     t.value = int(t.value)    
     return t
 
 # Define a rule so we can track line numbers
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)
 
 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
 # Error handling rule
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)
 
# Build the lexer
lexer = lex.lex()

# Build the Parser
parser = yacc.yacc()
 # Test it out

 
 # Give the lexer some input
while True:
 print(' compo>')   
 data=input()
 lexer.input(data)
 
 # Tokenize
 while True:
     tok = lexer.token()
     if not tok: 
        break      # No more input
     print(tok)