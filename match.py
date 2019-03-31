#Match regular expression to a string
import shunting
import thompsons
from state import state
from nfa import nfa


def match(infix, string):
  """Matches string to reg expression
  When start anchot operator('^') is used, RecursionError is thrown, this happens due to accept state pointing to itself.
  And it happens when expression evaluates to true, based on that try/except statment returns True by default and 
  enables ^ functionality. Not smartest or cleanest way but its working.
  """
  postfix = shunting.shunt(infix)
  nfa = thompsons.compile(postfix)

  current = set()
  next = set()

  current |= followes(nfa.initial)
  #Loop through each characeter
  for s in string:
    for c in current:
      if c.label == s:
        #Try statement to deal with RecursionError
        try:
          next |= followes(c.edge1)
        except RecursionError:
          return True
    current = next
    next = set()

  return (nfa.accept in current)
  
def followes(state):
  states = set()
  states.add(state)

  if state.label is None:

    if state.edge1 is not None:
      states |= followes(state.edge1)

    if state.edge2 is not None:
      states |= followes(state.edge2)

  return states    
