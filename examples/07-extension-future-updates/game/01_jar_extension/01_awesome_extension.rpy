init -999 python:
  class Jar(object):
    # tag::version_number[]
    VERSION = 1
    # end::version_number[]
    def __init__(self, initial_count = 0, maximum = None):
      self.count = initial_count
      self.maximum = maximum

    # tag::update[]
    def _update(self, state):
      version = state.pop('_version', 0)
      if version == Jar.VERSION:
        return
      if version <= 0:
        if 'maximum' not in state:
          state['maximum'] = None
      # Handle next versions updates here
    # end::update[]

    def __setstate__(self, state):
      self._update(state)
      self.__dict__ = state

    def _rollback(self, compressed):
      self.__dict__.clear()
      self.__dict__.update(compressed)
      self._update(self.__dict__)

    # tag::save[]
    def __getstate__(self):
      return self._clean()

    def _clean(self):
      data = self.__dict__.copy()
      data['_version'] = Jar.VERSION
      return data

    def _compress(self, clean):
      return clean
    # end::save[]

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
