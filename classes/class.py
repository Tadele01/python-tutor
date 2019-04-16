class countFromBy():
    def __init__(self, v:int=0, i:int=1)-> None:
        self.val = v
        self.incr = i
        
    def __repr__(self)->str:
        return str(self.val)
    def increase(self) -> None:
        self.val+= self.incr
    def decrease(self) -> None:
        self.val -= self.incr
a = countFromBy(100,10)
b = countFromBy(100,10)
c = countFromBy()
c.increase()
c.increase()
a.increase()
a.increase()
a.increase()
a.increase()
a.decrease()
b.increase()
print(a.val)
print(b.val)
print(c.val)