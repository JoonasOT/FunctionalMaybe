# FunctionalMaybe
A simple Maybe wrapper class that works. Creates a wrapper around variable and allows transformation of said variable to different values and supplying it to functions.

# Usage:
```Python
from FunctionalMaybe import FunctionalMaybe as Maybe

class Foo:
  def __init__:

joined = Maybe(["one", "two", "three"])\
              .transform(lambda list_: ", ".join(list_))\ # Transform the contained values to something else
              .run(lambda result: print(result))\         # Run functions with the contained value without altering the wrapped value
              .get()                                      # Return the wrapped value

```
