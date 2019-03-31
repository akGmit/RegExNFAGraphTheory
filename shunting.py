#Andrius Korsakas
#Shunting Yard Algorithm module
#As 

specials = {"*": 50, "|": 30, "?" : 50, '+': 50, '^': 35, '.': 40}

def shunt(infix):

  postfix = ""
  stack = ""
  infix = insertconcat(infix)
  for c in infix:
    if c == "(":
      stack = stack + c
    elif c == ")":
      while stack[-1] != "(":
        postfix, stack = postfix + stack[-1], stack[:-1]
      stack = stack[:-1]
    elif c in specials:
      while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
        postfix, stack = postfix + stack[-1], stack[:-1]
      stack = stack + c
    else:
      postfix = postfix + c
  while stack:
    postfix, stack = postfix + stack[-1], stack[:-1]
  print(postfix)
  return postfix

def insertconcat(infix):
  """A helper function converting user entered infix regular expression with inferred concatenation 
  to infix reg ex with concatenation operator inserted.

  param infix: A string representing infix reg ex without . operator
  type infix: str
  """
 
  pos = 0                             #Variable to follow current position in expression
  concatfix = ""                      #Infix expression with inserted concat operator
  for c in infix:
    next = pos + 1                    #Index of next character in infix expression
    
    #If next is not out of bounds
    if next < len(infix):
      nextc = infix[next]             #Next character in infix expression
      concatfix = concatfix + c       #Infix expression with inserted concat operators
  
      #If/elif statement to evaluate current and following characters in infix expression
      #and insert concat operator
      if (c.isalpha() or c.isdigit()) and (nextc.isalpha() or nextc.isdigit()):
        concatfix = concatfix + '.'
      elif c == ')' and (nextc.isalpha() or nextc.isdigit()):
        concatfix = concatfix + '.'
      elif c == ')' and nextc == '(':
        concatfix = concatfix + '.'
      elif (c.isalpha() or c.isdigit()) and nextc == '(':
        concatfix = concatfix + '.'
      elif c in '*?+':
        concatfix = concatfix + '.'
    #Else if its the last character, append it to converted infix reg ex
    else:
      concatfix = concatfix + c
    pos += 1

  return concatfix
