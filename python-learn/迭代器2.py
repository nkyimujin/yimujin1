class myNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        
        return x
myClass = myNumbers()
myIter = iter(myClass)
for x in myIter:
    print(x)
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))