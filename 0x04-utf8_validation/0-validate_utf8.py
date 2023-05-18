#!/usr/bin/python3

def validUTF8(data):
  """
  Returns True if the given data set represents a valid UTF-8 encoding, else returns False.

  Args:
    data: A list of integers representing the data set.

  Returns:
    True if data is a valid UTF-8 encoding, else False.
  """

  num_bytes = 0

  for byte in data:
      # Check if the byte is a continuation byte
      if num_bytes == 0:
          if byte >> 5 == 0b110:
              num_bytes = 1
          elif byte >> 4 == 0b1110:  
              num_bytes = 2
          elif byte >> 3 == 0b11110:
              num_bytes = 3
          elif byte >> 7 == 0b0:
              continue
          else:
              return False
      else:
          # Check if the byte is a valid continuation byte
          if byte >> 6 != 0b10:
              return False
          num_bytes -= 1

  # Check if there are any remaining bytes
  return num_bytes == 0