#Shunting Yard Algorithm module

specials = {"*": 50, "|": 30, "?" : 50, '+': 50, '^': 35, '.': 40}

def shunt(infix):
  specials = {"*": 50, "|": 30, "?" : 50, '+': 50, '^': 35, '.': 40}

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
  pos = 0
  concatfix = ""
  for c in infix:
    next = pos + 1
    
    if next < len(infix):
      nextc = infix[next]
      concatfix = concatfix + c
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
    else:
      concatfix = concatfix + c
    pos = pos + 1

  return concatfix
