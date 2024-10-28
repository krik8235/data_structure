import sys
sys.path.insert(0,"..")

from python_classes.linked_list import LinkedList
from python_classes.node import Node


class HashMap:
  """
  an array with hash code
  """
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]


  def hash(self, key, count_collisions=0):
    """
    convert a string into its corresponding bytes and return sum of the bytes
    add count_collisions to sum of key_bytes to determine the hash code to return.
    """
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions
    

  def compressor(self, hash_code):
    """
    Ensures that the index is valid and always within the bounds of the array by mapping a hash code to an array index.
    Returns a value between 0 and array_size - 1 by taking the modulus (%) of the hash code with the array size.
    """
    return hash_code % self.array_size
  

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    # self.array[array_index] = value

    """
    Address collision by storing k-v pair in the array
    """
    current_array_value = self.array[array_index]

    if current_array_value is None:
      # open addressing - place the new key-value pair into the hash map.
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    """
    When the key we’re trying to set (key) is different from python_classes.the key at our hash code’s address (current_array_value[0]), 
    create a new variable called number_collisions.
    And store new_hash_code in the array at new_array_index, incrementally increase number_collisions
    """
    number_collisions = 1
    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1
    return


  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    # return self.array[array_index]

    """Address collision - when the array item has kv pair - return only value """
    possible_return_value = self.array[array_index]
    if possible_return_value is None:
        return None

    if possible_return_value[0] == key:
        return possible_return_value[1]


    """
    Continue searching when possible_return_value has a different key than the one we’re looking for.
    Replicate the retrieval logic while increasing the count of retrieval_collisions to continue to look at other locations in the array.
    """
    retrieval_collisions = 1
    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      retrieval_collisions += 1

    return   
