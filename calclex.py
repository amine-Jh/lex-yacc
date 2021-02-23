import ply.lex as lex
from ply.lex import TOKEN
import ply.yacc as yacc
names={}

# la liste des tokens.  required 
tokens = (
    'ZA2ID','3ADAD',
    'MOTAGHAYIR','NA9IS',
    'DERB','9ISMA',
    '9AWSLISSER','9AWSLIMEN',
    'TOSSAWI','MA39OFALIMN',
    'MA39OFALISSER','AFFECT',
    'KBER','SGHER',
    'KLMA',
    'TOKHALIF'
    )

reserved = {
    'ida' : 'IDA','alors' : 'ALORS','wla' : 'WLA','baynama' : 'BAYNAMA',
    'minajl':'MINAJL','kteb':'KTEB','scan':'SCAN','w':'W',
    'aw': 'AW','khroj':'KHROJ','tabita':'TABITA','dir':'DIR'
    }
tokens+=tuple(reserved.values())
 # Regular expression rules for simple tokens
t_ZA2ID    = r'\+'
t_NA9IS   = r'\-'
t_DERB   = r'\*'
t_9ISMA  = r'/'
t_9AWSLISSER  = r'\('
t_9AWSLIMEN  = r'\)'
t_TOSSAWI =r'=='
t_TOKHALIF=r'!='
t_AFFECT =r'='
t_SGHER =r'<'
t_KBER=r'>'

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
def t_KLMA(t):
     r'[a-zA-Z][a-zA-Z_0-9]*'
     t.value=str(t.value)    # Check for reserved words
     return t
# Define a rule so we can track line numbers
t_ignore  = ' \t'
literals = ['{','}']
#new Line
def t_newline(t):
     r'\n+'
     print('value of line'+t.value)
     t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
def find_column(input,token):
     line_start = input.rfind('\n', 0, token.lexpos) + 1
     return (token.lexpos - line_start) + 1
# Error handling rule
def t_error(t):
     print("character mam3rofch '%s'" % t.value[0]) 
     t.lexer.skip(1)
# EOF handling rule
def t_eof(t):
     return None
def t_COMMENT(t):
     r'(\//|\#).*'
     pass


####################################
#################################
lexer = lex.lex()
###########################
############################

#if statement
def p_statement_ida(p):
     '''statement : IDA  9AWSLISSER comparaison 9AWSLIMEN '{' expression '}'  
     '''
     if(p[3]):
          p[0]=p[6]
#while statement
def p_statement_baynama(p):
     'statement : BAYNAMA 9AWSLISSER comparaison 9AWSLIMEN expression'
     while(p[3]):
          
          p[0]=p[5]
# comparaison
def p_comparaison(p):
     '''comparaison : expression KBER expression 
                    | expression SGHER expression
                    | expression TOSSAWI expression
                    | expression TOKHALIF expression
     '''
     if(p[2]=='>'):
          p[0]=p[1]>p[3]
     if(p[2]=='<'):
          p[0]=p[1]<p[3]
     if(p[2]=='=='):
          p[0]=p[1]==p[3]
     if(p[2]=='!='):
          p[0]=p[1]!=p[3]
     

def p_statement(p):
     '''  statement : expression   '''
     p[0]=p[1]

def p_statement_kteb(p):
     ''' statement : KTEB 9AWSLISSER expression 9AWSLIMEN   '''
     p[0]=p[3]

def p_statement_affect(p):
     'statement : MOTAGHAYIR AFFECT expression'
     p[0]=p[3]
     names[p[1]] =p[3]  
    

def p_expression_motaghayir(p):
    'expression : MOTAGHAYIR'
    # attempt to lookup variable in current dictionary, throw error if not found
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("variable makynch '%s'" % p[1])
        p[0] = 0




def p_expression_za2id(p):
     'expression : expression ZA2ID term'
     p[0] = p[1] + p[3]
 
def p_expression_na9is(p):
     'expression : expression NA9IS term'
     p[0] = p[1] - p[3]
 
def p_expression_term(p):
     '''expression : term'''
     p[0] = p[1]

 
def p_term_derb(p):
     'term : term DERB factor'
     p[0] = p[1] * p[3]
 
def p_term_9isma(p):
     'term : term 9ISMA factor'
     p[0] = p[1] / p[3]
 
def p_term_factor(p):
     '''term : factor
               
     '''
     
     p[0] = p[1]
 
def p_factor_3adad(p):
     '''factor : 3ADAD'''
     
     p[0] = p[1]

 
def p_factor_expr(p):
     'factor : 9AWSLISSER expression 9AWSLIMEN'
     p[0] = p[2]

 
# Error rule for syntax errors
def p_error(p):
     print("khata2 f syntax!")

def p_empty(p):
     'empty :  '
     pass 


precedence = (('nonassoc', 'KBER', 'SGHER'),
     ('left', 'ZA2ID', 'NA9IS'),
     ('left', 'DERB', '9ISMA'),
     ('right', 'UMINUS'),            # Unary minus operator
 )

def p_expr_uminus(p):
     'expression : NA9IS expression %prec UMINUS'
     p[0] = -p[2]


'''
while True:
 data= input("compiler >")
 lexer.input(data)
 

 for tok in lexer:
     print(tok)'''


 # Build the parser
parser = yacc.yacc(debug=True)
 
while True:
    try:
        s = input('parser>')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)



