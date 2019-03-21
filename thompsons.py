#Thompsons construction
from state import state
from nfa import nfa

def compile(postfix):
  nfastack = []

  for c in postfix:
    if c == '.':
      nfa2, nfa1 = nfastack.pop(), nfastack.pop()
      nfa1.accept.edge1 = nfa2.initial

      nfastack.append(nfa(nfa1.initial, nfa2.accept))
    
    elif c == '|':
      nfa2, nfa1 = nfastack.pop(), nfastack.pop()
      
      initial = state()
      initial.edge1 = nfa1.initial
      initial.edge2 = nfa2.initial

      accept = state()
      nfa1.accept.edge1 = accept
      nfa2.accept.edge2 = accept

      nfastack.append(nfa(initial, accept))
    
    elif c == '*':
      nfa1 = nfastack.pop()

      initial = state()
      accept = state()

      initial.edge1 = nfa1.initial
      initial.edge2 = accept

      nfa1.accept.edge1 = nfa1.initial
      nfa1.accept.edge2 = accept

      nfastack.append(nfa(initial, accept))

    elif c == '?':
      #Pop operand from stack
      nfa1 = nfastack.pop()
      #Create new initial and accept states
      initial = state()
      accept = state()
      #Connect new initial states edge1 to operands initial state
      #and edge2 to accept state 
      initial.edge1 = nfa1.initial
      initial.edge2 = accept
      #Popped operands accept state connected to new accept state
      nfa1.accept.edge1 = accept
      #Push new nfa on stack
      nfastack.append(nfa(initial, accept))

    else:
      accept = state()
      initial = state()

      initial.label = c
      initial.edge1 = accept

      nfastack.append(nfa(initial, accept))

  return nfastack.pop()


    