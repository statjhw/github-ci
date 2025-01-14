class Heap :
    def __init__(self) :
        self.data = []
        self.root_index = 1
        self.heap_size = 0
        self.data.append(-1)

    def is_empty(self) :
        if self.heap_size == 0 :
            return True
        else :
            return False
        
    def swap(self, idx1, idx2) :
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]
    
    def up_heap(self, idx) :
        if (idx == self.root_index) :
            return
        else :
            parent = idx // 2
            if self.data[parent] > self.data[idx] :
                self.swap(parent, idx)
                self.up_heap(parent)

    def down_heap(self, idx) :
        left = 2 * idx
        right = 2 * idx + 1

        if (right <= self.heap_size) :  #양쪽 모두 데이터가 있는 경우
            if self.data[left] <= self.data[right] :
                if self.data[left] < self.data[idx] :
                    self.swap(left, idx)
                    self.down_heap(left)
                else :
                    return
            else :
                if self.data[right] < self.data[idx] :
                    self.swap(right, idx)
                    self.down_heap(right)
                else :
                    return
        elif(left <= self.heap_size) : #left에만 데이터가 있는 겨우
            if self.data[left] < self.data[idx] :
                self.swap(left, idx)
                self.down_heap(left)
            else :
                return
        else :  #양쪽 모두 데이터가 없는 겨우
            return 
    
    def insert(self, e : int) -> int:
        self.data.append(e)
        self.heap_size += 1
        self.up_heap(self.heap_size)
    
    def remove_min(self) :
        top = self.data[self.root_index]
        self.data[self.root_index] = self.data[self.heap_size]
        self.heap_size -= 1
        self.down_heap(self.root_index)
        return top
    