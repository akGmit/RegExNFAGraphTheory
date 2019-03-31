"""
Andrius Korsakas
Thompsons construction algorithm
(based on video lectures)
"""
from state import state
from nfa import nfa

nfastack = []

def compile(postfix):
  """Main thomspons algorithm function dealing with postfix reg expresssion"""
  for c in postfix:
    if c == '.':
      concat()
    elif c == '|':
      alternate()
    elif c == '*':
      kleene()
    elif c == '?':
      zero_or_one()
    elif c =='+':
      one_or_more()
    elif c == '^':
      start_anchor()
    else:
      #Create nfa fragment for operand
      accept = state()
      initial = state()
      initial.label = c
      initial.edge1 = accept
      nfastack.append(nfa(initial, accept))

  return nfastack.pop()

def concat():
  """Concatenation('.') function.
  Pop two operands nfa's from stack, connect first operand accept state to second operand initial state.
  Push new nfa to nfastack.
  """
  nfa2, nfa1 = nfastack.pop(), nfastack.pop()
  nfa1.accept.edge1 = nfa2.initial
  nfastack.append(nfa(nfa1.initial, nfa2.accept))
    
def alternate():
  """Alternate('|') function
  Pop two operands nfa's from stack.
  Create new initial state, connect edge1 to nfa1 initial and edge2 to nfa2 initial - this way alternation is achieved.
  Create new accept state, nfa1 and nfa2 accept states are connected to new accept state.
  Push new nfa on nfastack
  """
  nfa1, nfa2 = nfastack.pop(), nfastack.pop()
  initial, accept = state(), state()
  initial.edge1, initial.edge2 = nfa1.initial, nfa2.initial
  nfa1.accept.edge1, nfa2.accept.edge1 = accept, accept
  nfastack.append(nfa(initial, accept))

def kleene():
  """Pop operands nfa from stack.
  Connect initial edge1 to operands initial state, edge2 to accept state(representing empty input).
  Loop back nfa1 accept state to its initial state(acceptin any number of elements)
  Push on nfa stack
  """
  nfa1 = nfastack.pop()
  initial, accept = state(), state()
  initial.edge1, initial.edge2 = nfa1.initial, accept
  nfa1.accept.edge1, nfa1.accept.edge2 = nfa1.initial, accept
  nfastack.append(nfa(initial, accept))

def zero_or_one():
  """Zero or more('?') function
  Pop operand from stack
  Connect new initial states edge1 to operands initial state and edge2 to accept state(zero or one) 
  Popped operands accept state connected to new accept state
  """
  nfa1 = nfastack.pop()
  initial, accept = state(), state()
  initial.edge1, initial.edge2 = nfa1.initial, accept
  nfa1.accept.edge1 = accept
  nfastack.append(nfa(initial, accept))

def one_or_more():
  """One or more('+') function
  Connect initial states edge1 to operands initial state, this becomes new initial state of nfa.
  Original nfa accept state edge1 to new accept state, and edge2 two to initial state.
  This way nfa accepts one or more .
  """
  nfa1 = nfastack.pop()
  initial, accept = state(), state()
  initial.edge1 = nfa1.initial
  nfa1.accept.edge1, nfa1.accept.edge2 = accept, nfa1.initial
  nfastack.append(nfa(initial, accept))

def start_anchor():
  """String start anchor('^') function.
  Initial state to nfa1 initial.
  Nfa1 accept edge1 to accept, nfa1 accept edge2 to itself.
  Because nfa accept state poits to itself it causes RecuresionError, this happens when string is matcged against reg ex.
  Dealing with error in match module, not the cleanest or smartest way but it works.
  """
  nfa1 = nfastack.pop()
  initial, accept = state(), state()
  initial.edge1 = nfa1.initial
  nfa1.accept.edge1, nfa1.accept.edge2 = accept, nfa1.accept
  nfastack.append(nfa(initial, accept))