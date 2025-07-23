class Node[T]:
    def __init__(self, value: T):
        self.value = value

    def unpack(self) -> T:
        return self.value
    
