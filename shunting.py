#Shunting Yard Algorithm module


def shunt(infix):
  specials = {"*": 50, ".": 40, "|": 30, "?" : 50}

  postfix = ""
  stack = ""

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

  return postfix
