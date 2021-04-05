class MinHeap:
    """
    array based min heap implementation of a priority queue
    Things to note:
    1) left child, right child, and parent indexing with 2*i, 2*i+1, i//2
    does not work if the array starts at index 0. ex:
    index  1 and 2 should have parent 0, but 2//1 = 1 which is wrong
    we need a placeholder, say None, at index 0 then add elements starting at 1.

    2) queue is implemented as an python list. len() attribute is called often
    in the minHeap methods. This is fine. Python augments their lists with a len
    attribute that is both maintained and accessible in O(1) time.
    """

    def __init__(self):
        """Initialy empy heap"""
        self.queue = [None]
        self.min_index = None
        self.size = 0

    def __len__(self):
        """Define len method"""
        #account for None element at index 0
        return len(self.queue) -1

    def parent (self, pos):
        """Get the index of a node's parent"""
        return pos//2

    def leftChild(self, pos):
        """Get the index of a node's left child"""
        return pos * 2

    def rightChild(self, pos):
        """Get the indes of a node's right child"""
        return pos * 2 + 1

    def isLeaf(self, pos):
        """Check if a node is a leaf"""
        if pos > len(self)//2 and pos <= len(self)-1:
            return True
        return False

    def swap(self, pos1, pos2):
        """Swap the value of two nodes"""
        if pos1==0 or pos2==0:
            raise IndexError('cant access element 0 of the queue')
        self.queue[pos1], self.queue[pos2] = self.queue[pos2], self.queue[pos1]

    def insert(self, element):
        """Insert a value into the min heap, move this value up the heapify
        to maintain the minheap property"""
        self.queue.append(element)
        print('queue after insert {}'.format(self.queue))
        current = len(self)
        print('current {}'.format(current))
        #need to drag this newly inserted value up the min heap
        while current!=1 and self.queue[current] < self.queue[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
            print('floating elemnt up: {}'.format(self.queue))

    def minHeapify(self, pos):
        """Check if a node is greater than both of its children, if so,
        correct this obstruction of the min heap property"""
        #check if node has child, ie  is not a isLeaf

        if not self.isLeaf(pos):
            #if parent is bigger than either child
            if self.queue[pos]>self.queue[self.leftChild(pos)] or self.queue[pos]>self.queue[self.rightChild(pos)]:
                #swap with the larger of the children
                #if left child is bigger swap with left child
                print(self.leftChild(pos))
                if self.queue[self.leftChild(pos)] < self.queue[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    minHeapify(self.rightChild(pos))

    def buildMinHeap(self):
        """Loop through all nodes in the min heap that are not leaves,
        check of the min heap property is satisfied, if not, correct with
        minHeapify"""
        for i in range((self.size-1)//2, -1, -1):
            print('size=',self.size)
            print('minheapifying at', i)
            self.minHeapify(i)

    def __str__(self):
        return str(self.queue)

    def Print(self):
        for i in range(1, (self.size//2)):
            print(" PARENT : "+ str(self.queue[i])+" LEFT CHILD : "+
                                str(self.queue[2 * i])+" RIGHT CHILD : "+
                                str(self.queue[2 * i + 1]))



test = MinHeap()
for i in range(10, 0, -1):
    print('inserting {}'.format(i))
    test.insert(i)
test.buildMinHeap()
#print(test)
