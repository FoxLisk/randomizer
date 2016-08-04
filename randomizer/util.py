# f: a -> [b]
# l: [a]
def flatmap(f, l):
  for el in l:
    for sub_el in f(el):
      yield sub_el
