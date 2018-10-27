
class LRUNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LRUCache:
    
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.head = LRUNode(None, None)
        self.tail = LRUNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.count = 0
        self.capacity = capacity
        self.cache = {}
    
    def print_list(self):
        print('*****************')
        node = self.head
        print('head to tail:')
        while node != self.tail:
            print('({}:{})'.format(node.key, node.value), '->', end = ' ')
            node = node.next
        print()
        print('tail to head:')
        node = self.tail
        while node != self.head:
            print('({}:{})'.format(node.key, node.value), '->', end = ' ')
            node = node.prev
        print()
        print('--------------------')
        
        
    def _detach_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None
        
    def _remove_tail(self):
        assert(self.count > 0)
        delNode = self.tail.prev
        self._detach_node(delNode)
        del delNode
        self.count -= 1
        return

    def _move_to_head(self, Node):
        assert(Node is not None)
        Node.prev = self.head
        Node.next = self.head.next
        self.head.next.prev = Node
        self.head.next = Node
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        print('get', key)
        self.print_list()
        node = self.cache.get(key, None)
        if node is None:
            return -1
        result = node.value
        
        self._detach_node(node)
        self._move_to_head(node)
        self.print_list()
        
        return result
    
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        print('set', key, value)
        self.print_list()
        node = self.cache.get(key, None)
        if node is not None:
            node.value = value
            self._detach_node(node)
            self._move_to_head(node)
            
        else:
            if self.count >= self.capacity:
                self._remove_tail()
            newNode = LRUNode(key, value)
            self.cache[key] = newNode
            self._move_to_head(newNode)
            self.count += 1
            
        self.print_list()


c = LRUCache(2)
c.set(2, 1)
c.set(1, 1)
c.get(2)
c.set(4, 1)
c.get(1)
c.get(2)
