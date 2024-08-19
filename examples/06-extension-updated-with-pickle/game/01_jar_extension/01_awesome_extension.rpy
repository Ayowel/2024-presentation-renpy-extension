init -999 python:
  class Jar(object):
    def __init__(self, initial_count = 0, maximum = None):
      self.count = initial_count
      self.maximum = maximum

    # tag::update[]
    def _update(self, state):
      if 'maximum' not in state:
        state['maximum'] = None

    def __setstate__(self, state):
      self._update(state)
      self.__dict__ = state

    def _rollback(self, compressed):
      self.__dict__.clear()
      self.__dict__.update(compressed)
      self._update(self.__dict__)
    # end::update[]

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
