from graphite.intervals import IntervalSet, Interval


class Node:
  name = property(lambda self: self.path.split('.')[-1])

  def __repr__(self):
    return '<%s: %s>' % (self.__class__.__name__, self.path)


class BranchNode(Node):
  is_leaf = False

  def __init__(self, path):
    self.path = path


class LeafNode(Node):
  is_leaf = True

  def __init__(self, path, reader):
    self.path = path
    self.reader = reader
    self.intervals = reader.get_intervals()

  def fetch(self, startTime, endTime):
    return self.reader.fetch(startTime, endTime)