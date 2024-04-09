class Rectangle:
    
    def __init__(self,length:int,width:int) -> None:
        self.length=length
        self.width=width
        self._index=0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self._index==0:
            self._index+=1
            return {'lenght':self.length}
        if self._index==1:
            self._index+=1
            return {'width':self.width}
        raise StopIteration
    
rect=Rectangle(10,5)
for a in rect:
    print(a)