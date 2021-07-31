""" Wrapper for common comms interfaces

Classes:
    - Comms: Abstract base class for all comms classes
"""
from abc import ABC, abstractmethod

class Comms(ABC):
    """ Base comms interface
    Methods:
        - open
        - close
        - write
        - read
    """

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def read(self, num_bytes):
        pass

# Maybe use this for functional testing of the classes in this file,
# not sure if this is good practice though
if __name__ == '__main__':
    pass
