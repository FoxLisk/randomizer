from collections import defaultdict
import tool

class Openable(object):
  def __init__(self, name, requires=None):
    self.name = name
    self.requires = requires

  def openable_with(self, tools):
    return self.requires is None or self.requires in tools

  def __str__(self):
    if self.requires is None:
      return self.name
    return '%s (%s)' % (self.name, self.requires)


class Location(object):
  def __init__(self, name):
    self.name = name
    self.links = defaultdict(list)
    self.openables = []

  def add_link(self, next_loc, *tools):
    f = frozenset(tools)
    self.links[f].append(next_loc)

  def add_openable(self, openable):
    self.openables.append(openable)

  def openable_with(self, tools):
    yield from (o for o in self.openables if o.openable_with(tools))

  def reachable_by(self, tools):
    reachable = [self]
    toolset = frozenset(tools)
    for required, locs in self.links.items():
      if required.issubset(toolset):
        for loc in locs:
          reachable.extend(loc.reachable_by(tools))
    assert len(reachable) == len(set(reachable))
    return reachable

  def tools_that_expand(self, tools):
    toolset = frozenset(tools)
    additions = set()
    for required, locs in self.links.items():
      if required.issubset(toolset):
        continue
      additions.add(required - toolset)
    return additions

  def __str__(self):
    return self.name

start = Location('start')
start.add_openable(Openable('pot1'))
start.add_openable(Openable('dear-old-dad'))

hyrule_castle_entrance = Location('castle-1')
start.add_link(hyrule_castle_entrance, tool.sword)

hyrule_basement = Location('castle-basement')
start.add_link(hyrule_castle_entrance, tool.castle_big_key)
