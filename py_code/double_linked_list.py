import sys
sys.path.insert(0,"..")

from python_classes.node import Node

class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
  

  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    self.head_node = new_head

    if self.tail_node == None:
      self.tail_node = new_head


  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail


  def remove_head(self):
    removed_head = self.head_node

    if removed_head == None:
      return None

    self.head_node = removed_head.get_next_node()

    if self.head_node != None:
      self.head_node.set_prev_node(None)

    if removed_head == self.tail_node:
      self.remove_tail()

    return removed_head.get_value()

  
  def remove_tail(self):
    removed_tail = self.tail_node

    if removed_tail == None:
      return None

    self.tail_node = removed_tail.get_prev_node()

    if self.tail_node != None:
      self.tail_node.set_next_node(None)

    if removed_tail == self.head_node:
      self.remove_head()

    return removed_tail.get_value()

  
  def remove_by_value(self, value_to_remove):
    """
    feature to remove middle value in the list
    """
    node_to_remove = None
    current_node = self.head_node

    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break

      current_node = current_node.get_next_node()


    if node_to_remove == None:
      return None
    
    else:
      if node_to_remove == self.head_node:
        self.remove_head()
      elif node_to_remove == self.tail_node:
        self.remove_tail()
      else:
        """
        Now we know that the node is somewhere in the middle of the list. To remove it, we will need to reset the pointers for the nodes around it.
        """
        next_node = node_to_remove.get_next_node()
        prev_node = node_to_remove.get_prev_node()

        """
        remove the pointers to and from node_to_remove and have next_node and prev_node point to each other.
        """
        next_node.set_prev_node(prev_node) #
        prev_node.set_next_node(next_node)
      
      return node_to_remove
     

  def stringify_list(self):
      string_list = ""
      current_node = self.head_node
      while current_node:
        if current_node.get_value() != None:
          string_list += str(current_node.get_value()) + "\n"
        current_node = current_node.get_next_node()
      return string_list



def make_dll(doubly_linked_list, random_value):
  """
  make dll
  """
  dll = DoublyLinkedList()
  head_value = doubly_linked_list.remove_head()
  tail_value = doubly_linked_list.remove_tail()
  dll.add_to_head(head_value)
  dll.add_to_tail(tail_value)
  dll.add_to_head(random_value)
  return dll



def add_n_strings_to_tail(doubly_linked_list, n):
  """
  add a string value to the tail for n times 
  """
  while  n > 0:
    doubly_linked_list.add_to_tail("f") 
    n = n - 1
