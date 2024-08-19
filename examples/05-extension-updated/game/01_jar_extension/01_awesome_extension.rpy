init -999 python:
  class Jar(object):
    def __init__(self, initial_count = 0, maximum = None):
      self.count = initial_count
      self.maximum = maximum

    def add(self, added = 1):
      assert added >= 0
      self.count += added
      if self.maximum is not None and self.count > self.maximum:
        raise Exception("Overfull Jar")

    def take(self, taken = 1):
      assert taken >= 0
      if self.count < taken:
        raise Exception("Underfull jar")
      self.count -= taken
