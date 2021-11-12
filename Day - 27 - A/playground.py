# became tupple
def add(*args):
    print(sum(args))


add(3, 5, 6, 18)
# became dictionary - **kwargs
def calculate(n, **kwargs):
    n +=kwargs['add']
    n *=kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5 )

class Tawo():

    def __init__(self, **kw):
        self.height = kw.get("height")
        self.name = kw.get("name")
        self.race = kw.get("race")


an_tawo = Tawo(height=52, name="Romeo", race="Asian")
print(an_tawo.name)


