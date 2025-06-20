class Solution:
    def calPoints(self, operations: List[str]) -> int:
        b = []
        for i in range(len(operations)):
            if operations[i] == '+':
                b.append(b[-1] + b[-2])
            elif operations[i] == 'D':
                b.append(2 * b[-1])
            elif operations[i] == 'C':
                b.pop()
            else:
                b.append(int(operations[i]))
        return sum(b)
        
