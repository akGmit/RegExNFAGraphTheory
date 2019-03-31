"""Class representing NFA with its states"""
class nfa:
  initial = None
  accept = None

  def __init__(self, initial, accept):
    self.initial = initial
    self.accept = accept