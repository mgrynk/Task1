class People(object):
  def __init__(self, dictionary):
    for key, value in dictionary.items():
      if isinstance(value, (list, tuple)):
        setattr(self, key, [People(x) if isinstance(x, dict) else x for x in value])
      else:
        setattr(self, key, People(value) if isinstance(value, dict) else value)
    else:
      setattr(self, key, People(value) if isinstance(value,dict)else value)
