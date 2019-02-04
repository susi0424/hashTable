"""LinkedList Implementation"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        cur = self.head
        if self.head:
            while cur.next:
                cur = cur.next
            cur.next = new_node
        else:
            self.head = new_node

    def get_node(self, position):
        count = 1
        cur = self.head
        if position < 1:
            return None
        while cur and count <= position:
            if count == position:
                return cur
            cur = cur.next
            count += 1
        return None

    def search(self, value):
        cur = self.head
        while cur.value != value and cur.next:
            cur = cur.next
        if cur.value == value:
            return True
        else:
            return False

    def insert(self, new_node, position):
        count = 1
        cur = self.head
        if position > 1:
            while cur and count < position:
                if count == position - 1:
                    new_node.next = cur.next
                    cur.next = new_node
                cur = cur.next
                count += 1
        elif position == 1:
            new_node.next = self.head
            self.head = new_node

    def print_all(self):
        cur = self.head
        while cur:
            print cur.value
            cur = cur.next

    def get_len(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def delete(self, value):
        cur = self.head
        prev = None
        while cur.value != value and cur.next:
            prev = cur
            cur = cur.next
        if cur.value == value:
            if prev:
                prev.next = cur.next
            else:
                self.head = cur.next



"""HashTable class"""

import random, string, numpy

class PlatesHash:
    
    def __init__(self, bucketSize=10):
        self.buckets = []
        [self.buckets.append(LinkedList()) for i in range(0, bucketSize)]
        
        
    def insert(self, value):
        hashIndex = self.__getHashIndex(value)
        self.buckets[hashIndex].insert(Node(value), 1) #always add node at head: O(1)
        
    def delete(self, value):
        hashIndex = self.__getHashIndex(value)
    
    def search(self, value):
        hashIndex = self.__getHashIndex(value)
        resultList = self.__get(hashIndex)
        return resultList.search(value)
        
    def visualizeHash(self):
        for i in range(0, len(self.buckets)):
            print str(i) + ': '
            self.buckets[i].print_all()
    
    def evaluateHashedResult(self):
        distribution = []
        [distribution.append(resultList.get_len()) for resultList in self.buckets]
        return numpy.std(distribution)
    
    '''Private functions'''
    def __get(self, index):
        return self.buckets[index]
    
    # hash function
    def __getHashIndex(self, value):
        asciiSum = weight = 0
        for char in value:
            weight += 1
            if weight in [2, 3, 4]:
                asciiSum += int(ord(char))*weight*3
            else:
                asciiSum += int(ord(char))*weight
        hashIndex = asciiSum%len(self.buckets)
        return hashIndex
        
        
# Generate plate numbers for California state format: 1ABC234
def generateRandomPlateNumbers(length=10):
    platesList = []
    for number in range(0, length):
        plateNumber = ''.join(random.sample(string.digits, 1))
        plateNumber += ''.join(random.sample(string.ascii_letters.upper(), 3))
        plateNumber += ''.join(random.sample(string.digits, 3))
        platesList.append(plateNumber)
    return platesList

if __name__ == "__main__":
    platesList = generateRandomPlateNumbers(75)
    platesHash = PlatesHash(bucketSize=50)
    [platesHash.insert(plateNumber) for plateNumber in platesList]
    platesHash.visualizeHash()
    print platesHash.evaluateHashedResult()


