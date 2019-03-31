"""
Andrius Korsakas
Shunting Yard Algorithm module
(shunt function based on video lectures)
"""

#Special reg ex operators and their precedence
specials = {"*": 50, "|": 30, "?" : 50, '+': 50, '^': 35, '.': 40}

def shunt(infix):
  """A function to convert infix regular expression to postfix.
  Takes user entered reg ex passes it to insertconcat helper function for concat processing.
  Converts infix reg ex to postfix.

  :param infix: A string representing infix regular expression with concatenation inferred
  :tyoe infix: str
  """
  postfix = ""                      
  stack = ""
  infix = insertconcat(infix)
  #For every character in infix 
  for c in infix:
    #Push opening bracket to stack
    if c == "(":
      stack = stack + c
    
    #If c is closing bracket
    #While last character of stack is not opening bracket
    #Pop elements from stack and add them to postfix
    #Discard closing opening bracket
    elif c == ")":
      while stack[-1] != "(":
        postfix, stack = postfix + stack[-1], stack[:-1]
      stack = stack[:-1]
    
    #If c is special character
    #If its precedence is less than or equal to the precedence of 
    #last operator on the stack, take operators from stack with greater precedence
    #and push them on stack.
    #Finally push current operator on stack
    elif c in specials:
      while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
        postfix, stack = postfix + stack[-1], stack[:-1]
      stack = stack + c
    #Push operand on stack
    else:
      postfix = postfix + c
  
  #If there is anything left on the stack
  #push all to postfix
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
      
      #Boolean variables repressentig if current or next character is letter/digit
      cisLetterOrDigit = (c.isalpha() or c.isdigit())
      nextcIsLetterOrDigit = (nextc.isalpha() or nextc.isdigit())
      
      #If/elif statement to evaluate current and following characters in infix expression
      #and insert concat operator
      if cisLetterOrDigit and nextcIsLetterOrDigit:
        concatfix += '.'
      elif c == ')' and nextcIsLetterOrDigit:
        concatfix += '.'
      elif c == ')' and nextc == '(':
        concatfix += '.'
      elif cisLetterOrDigit and nextc == '(':
        concatfix += '.'
      # elif c in '*?+':
      #   concatfix += c
    #Else if its the last character, append it to converted infix reg ex
    else:
      concatfix = concatfix + c
    pos += 1
  print(concatfix)
  return concatfix
