import ply.lex as lex
from ply.lex import TOKEN
import ply.yacc as yacc
 
 # List of token names.   This is always required


tokens = (
    
    'ZA2ID',
    '3ADAD',
    'MOTAGHAYIR',
    'NA9IS',
    'DERB',
    '9ISSMA',
    '9AWSLISSER',
    '9AWSLIMEN',
    'TOSSAWI',
    'MA39OFALIMN',
    'MA39OFALISSER',
    'AFFECT'
    )
reserved = {
    'ida' : 'IDA',
    'alors' : 'ALORS',
    'wla' : 'WLA',
    'baynama' : 'BAYNAMA',
    'minajl':'MINAJL',
    
    
    'kteb':'KTEB',
    'scan':'SCAN',
    'w':'W',
    'aw': 'AW',
    'khroj':'KHROJ',
    'tabita':'TABITA',
    'dir':'DIR'
}

tokens+=tuple(reserved.values())
 # Regular expression rules for simple tokens
t_ZA2ID    = r'\+'
t_NA9IS   = r'\-'
t_DERB   = r'\*'
t_9ISSMA  = r'/'
t_9AWSLISSER  = r'\('
t_9AWSLIMEN  = r'\)'
t_TOSSAWI =r'=='
t_AFFECT =r'='



def t_MA39OFALISSER(t):
     r'\{'
     t.type = '{'      # Set token type to the expected literal
     return t
 
def t_MA39OFALIMN(t):
     r'\}'
     t.type = '}'      # Set token type to the expected literal
     return t

 # A regular expression rule with some action code

def t_3ADAD(t):
     r'\d+'
     t.value = int(t.value)    
     return t

def t_MOTAGHAYIR(t):
     r'[a-zA-Z][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'MOTAGHAYIR')    # Check for reserved words
     return t
 
 # Define a rule so we can track line numbers
def t_newline(t):
     r'\n+'
     print('value of line'+t.value)
     t.lexer.lineno += len(t.value)
 
 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
literals = ['+','-','*','/','{','}']

# Compute column.
 #     input is the input text string
 #     token is a token instance
def find_column(input, token):
     line_start = input.rfind('\n', 0, token.lexpos) + 1
     return (token.lexpos - line_start) + 1


 # Error handling rule
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

 # EOF handling rule
def t_eof(t):
     # Get more input (Example)
     
     more = input("....   ")
     if more:
         lexer.input(more)
         return lexer.token()
     return None
def t_COMMENT(t):
     r'(\//|\#).*'
     pass
     # No return value. Token discarded
# Build the lexer
lexer = lex.lex(debug=1)

# Build the Parser

 # Test it out


 # Give the lexer some input
while True:
    
 data=input(" compiler >")
 lexer.input(data)
 
 # Tokenize
 for tok in lexer:
     print(tok)