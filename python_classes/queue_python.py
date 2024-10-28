import sys
sys.path.insert(0,"..")

from python_classes.node import Node

class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0


  def enqueue(self, value):
    """add an element"""

    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")


  def dequeue(self):
    """remove an element"""

    if self.get_size() > 0:
      item_to_remove = self.head
      print(str(item_to_remove.get_value()) + " is served!")
      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("The queue is totally empty!")


  def peek(self):
    """look at the front element"""

    if self.size > 0:
      return self.head.get_value()
    else:
      print("No orders waiting!")
  

  def get_size(self):
    return self.size
  

  def has_space(self):
    """useful method to see if we can .enqueue() a new value on the end of the queue."""

    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    

  def is_empty(self):
    """useful method to prevent queue underflow (trying to dequeue from empty queue)"""
    return self.size == 0