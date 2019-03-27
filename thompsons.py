#Thompsons construction
from state import state
from nfa import nfa

specials = {"*": 50, "|": 30, "?" : 50, '+': 50, '$': 40}

def compile(postfix):
  nfastack = []
  pos = 0
  for c in postfix:
    
    if c == '.':

      nfa2 = nfastack.pop()
      nfa1 = nfastack.pop()

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

    elif c =='+':
      #Pop operand from stack
      nfa1 = nfastack.pop()
      #Create new initial and accept states
      initial = state()
      accept = state()

      #Connect initial states edge1 to operands initial state, this becomes new initial state of nfa
      initial.edge1 = nfa1.initial
      #Original nfa accept state edge1 to new accept state, and edge2 two to initial state
      #This way nfa accepts one or more 
      nfa1.accept.edge1 = accept
      nfa1.accept.edge2 = nfa1.initial

      nfastack.append(nfa(initial, accept))

    else:
      
      # #If one operand is already in stack, then we can pop it and concat to current operand in postfix
      # if len(nfastack) == 1:
      #   #Pop operand from stack
      #   nfa1 = nfastack.pop()

      #   #Take current operand from postfix and create nfa
      #   accept = state()
      #   initial = state()
      #   initial.label = c
      #   initial.edge1 = accept
      #   nfa2 = nfa(initial, accept)

      #   nfa1.accept.edge1 = nfa2.initial

      #   nfastack.append(nfa(nfa1.initial, nfa2.accept))
      # else:
      accept = state()
      initial = state()
      initial.label = c
      initial.edge1 = accept

      nfastack.append(nfa(initial, accept))

      pos = pos + 1

  return nfastack.pop()


    