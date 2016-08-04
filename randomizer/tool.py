class Tool(object):
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

  def __repr__(self):
    return self.name

sword = Tool('sword')
castle_big_key = Tool('castle-big-key')
