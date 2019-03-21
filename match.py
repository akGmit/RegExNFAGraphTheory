#Match regular expression to a string
import shunting
import thompsons
from state import state
from nfa import nfa


def match(infix, string):
  postfix = shunting.shunt(infix)
  nfa = thompsons.compile(postfix)

  current = set()
  next = set()

  current |= followes(nfa.initial)

  for s in string:
    for c in current:
      if c.label == s:
        next |= followes(c.edge1)

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
