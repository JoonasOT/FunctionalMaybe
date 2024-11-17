# FunctionalMaybe
A simple Maybe wrapper class that works. Creates a wrapper around variable and allows transformation of said variable to different values and supplying it to functions.

# Usage:
```Python
from FunctionalMaybe import FunctionalMaybe as Maybe


joined = Maybe(["one", "two", "three"])\
              .transform(lambda list_: ", ".join(list_))\ # Transform the contained values to something else
              .run(lambda result: print(result))\         # Run functions with the contained value
              .get()                                      # Return the wrapped value

```

Also supports calling the constructure inside the Maybe-class, which enables error handling via Maybe.Empty:
```Python
from FunctionalMaybe import FunctionalMaybe as Maybe

class Foo:
    def __init__(self, x, y, z=None, w=1):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}, {self.w}"

def log(val):
    print(val)

Maybe().construct(Foo, 1, "one", w=4).transform(lambda foo: str(foo)).run(log)

```
