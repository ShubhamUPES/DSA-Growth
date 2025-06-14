class MyHashSet:

    def __init__(self):
        self.myhashset = []

    def add(self, key: int) -> None:
        if key not in self.myhashset:
            self.myhashset.append(key)

    def remove(self, key: int) -> None:
        if key in self.myhashset:
            self.myhashset.remove(key)

    def contains(self, key: int) -> bool:
        for i in range(len(self.myhashset)):
            if self.myhashset[i] == key:
                return True
        return False
