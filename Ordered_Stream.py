''' Design an ordered Stream '''
class OrderedStream:

    def __init__(self, n: int):
        self.st = [None]*(n+1)
        self.pt = 1
    def insert(self, idKey: int, value: str) :
        self.st[idKey] = value
        result = []
        while self.pt < len(self.st) and self.st[self.pt] :
            result.append(self.st[self.pt])
            self.pt += 1
        return result
# Your OrderedStream object will be instantiated and called as such:
n = 5
obj = OrderedStream(n)
obj.insert(3,'ccccc')
obj.insert(1,'aaaaa')
obj.insert(2,'bbbbb')
obj.insert(5,'eeeee')
print(obj.insert(4,'ddddd'))
