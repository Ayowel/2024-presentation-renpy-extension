init python:
  class Jar(object):
    def __init__(self, initial_count = 0):
      self.count = initial_count

    def add(self, added = 1):
      assert added >= 0
      self.count += added

    def take(self, taken = 1):
      assert taken >= 0
      if self.count < taken:
        raise Exception("Underfull jar")
      self.count -= taken
