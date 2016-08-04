from location import start
from util import flatmap
from tool import sword

def randomize():
  placed = [sword]
  reachable_so_far = start.reachable_by(placed)
  print([str(l) for l in reachable_so_far])
  openables = flatmap(lambda l: l.openable_with(placed), reachable_so_far)
  print([str(o) for o in openables])
  to_place = flatmap(lambda l: l.tools_that_expand(placed), reachable_so_far)
  to_place = set(to_place)
  print(to_place)


randomize()
