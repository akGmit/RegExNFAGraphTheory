#Shunting Yard Algorithm module


def shunt(infix):
  specials = {"*": 50, "|": 30, "?" : 50, '+': 50, '^': 35, '.': 40}

  postfix = ""
  stack = ""
  op = 0
  for c in infix:
    if c == "(":
      #op = op + 1
      stack = stack + c
    elif c == ")":
      #op = op - 1
      while stack[-1] != "(":
        postfix, stack = postfix + stack[-1], stack[:-1]
      stack = stack[:-1]
      
    elif c in specials:
      while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
        postfix, stack = postfix + stack[-1], stack[:-1]
      stack = stack + c
    else:
      #if op > 1:
        #postfix = postfix + '.'
        #op = 0
      postfix = postfix + c
      #op = op + 1

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
      concatfix = concatfix + c
      if c.isalpha() and infix[next].isalpha():
        concatfix = concatfix + '.'
      elif c == ')' and infix[next].isalpha():
        concatfix = concatfix + '.'
      elif c == ')' and infix[next] == '(':
        concatfix = concatfix + '.'
      elif c.isalpha() and infix[next] == '(':
        concatfix = concatfix + '.'
    else:
      concatfix = concatfix + c
    pos = pos + 1

  return concatfix
