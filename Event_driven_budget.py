class ExpenseRequest:
    def __init__(self, description: str, department: str ,amount: float, priority: int):
        self.description = description
        self.department = department
        self.amount = amount
        self.priority = priority

    def __repr__(self):
        return f"[Priority: {self.priority}] {self.department} - {self.description}: ${self.amount}"


class HeapManagment:
    def __init__(self):
        self.heap = []
    
    def parent(self, index):
        return (index - 1) // 2

    def leftChild(self, index):
        return (index * 2) + 1

    def rightChild(self, index):
        return (index * 2) + 2

    #helper function for heapifyUp
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, request: ExpenseRequest):
        self.heap.append(request)
        self.heapifyUp(len(self.heap) - 1)

    #moves the inserted object up if we are not at a root and the object's priotiy is higher than its parent's
    def heapifyUp(self, index):

        parentIndex = self.parent(index)

        if index > 0 and self.heap[index].priority > self.heap[parentIndex].priority:
            self.swap(index, parentIndex)
            #recursively check the new position compared to the new parent
            self.heapifyUp(parentIndex)

    def removeMax(self):
        if len(self.heap) == 0:
            return None

        maxVal = self.heap[0]

        lastItem = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = lastItem
            self.heapifyDown(0)
        
        return maxVal


    def heapifyDown(self, index):
        largest = index
        leftIndex = self.leftChild(index)
        rightIndex = self.rightChild(index)

        if leftIndex < len(self.heap) and self.heap[largest].priority < self.heap[leftIndex].priority:
            largest = leftIndex

        if rightIndex < len(self.heap) and self.heap[largest].priority < self.heap[rightIndex].priority:
            largest = rightIndex

        if largest != index:
            self.swap(index, largest)
            self.heapifyDown(largest)
            
            



