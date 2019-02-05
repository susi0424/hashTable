import random, string, numpy


""" LinkedList Implementation """

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    ''' Append a new node at the end '''
    def append(self, newNode):
        cur = self.head
        if self.head:
            while cur.next:
                cur = cur.next
            cur.next = newNode
        else:
            self.head = newNode
    
    ''' Get a node at given position '''
    def getNode(self, position):
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
    
    ''' Check if a given value exists in any node of the LinkedList.
        Return True/False 
    '''
    def search(self, value): 
        cur = self.head
        while cur and cur.value != value and cur.next:
            cur = cur.next
        if cur and cur.value == value:
            return True
        else:
            return False
    
    ''' Insert a node at given position (1 based) '''
    def insert(self, newNode, position):
        count = 1
        cur = self.head
        if position > 1:
            while cur and count < position:
                if count == position - 1:
                    newNode.next = cur.next
                    cur.next = newNode
                cur = cur.next
                count += 1
        elif position == 1:
            newNode.next = self.head
            self.head = newNode

    ''' Print all node values '''
    def printAll(self):
        printStr = ''
        cur = self.head
        while cur:
            printStr += cur.value + ' -> '
            cur = cur.next
        print printStr

    ''' Get the length of LinkedList '''
    def getLen(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    ''' Delete a node with specific value '''
    def delete(self, value):
        cur = self.head
        prev = None
        while cur and cur.value != value and cur.next:
            prev = cur
            cur = cur.next
        if cur and cur.value == value:
            if prev:
                prev.next = cur.next
            else:
                self.head = cur.next



""" HashTable Class """
class PlatesHash:
    
    ''' Initialize a hash table with a given bucket size '''
    def __init__(self, bucketSize=10):
        self.keyTotal = 0
        self.buckets = []
        [self.buckets.append(LinkedList()) for i in range(0, bucketSize)]
        
    ''' Insert a plate (numbers) into a bucket (list) as a LinkedList node '''    
    def insert(self, value, reHash=True):
        hashIndex = self.__getHashIndex(value)
        self.buckets[hashIndex].insert(Node(value), 1) # Always add node at head: O(1)
        self.keyTotal += 1
        if reHash and self.__needReHash() is not None:
            self.__reHash(self.__needReHash())
        else:
            pass
    
    ''' Delete a plate from the bucket '''    
    def delete(self, value, reHash=True):
        hashIndex = self.__getHashIndex(value)
        self.buckets[hashIndex].delete(value)
        self.keyTotal -= 1
        if reHash and self.__needReHash() is not None:
            self.__reHash(self.__needReHash())
        else:
            pass
    
    ''' Check if a specific plate exists in any bucket.
    Return True/False
    '''
    def search(self, value):
        hashIndex = self.__getHashIndex(value)
        resultList = self.__get(hashIndex)
        return resultList.search(value)
    
    ''' Print all results of the Hash Table '''    
    def visualizeHash(self):
        for i in range(0, len(self.buckets)):
            print str(i) + ': ',
            self.buckets[i].printAll()
    
    ''' Use Standard Deviation to Evaluate the result distribution of hash table '''
    def evaluateHashedResult(self):
        distribution = []
        [distribution.append(resultList.getLen()) for resultList in self.buckets]
        return numpy.std(distribution) # Standard Deviation of all LinkedLists Length
    
    def getBuckets(self):
        return self.buckets
    
    ''' Get the LinkedList from a bucket '''
    def __get(self, index):
        return self.buckets[index]
    
    ''' Hash function: return hashed value
    (Input: a plate - assume California format eg:1ABC234)
    1. Get ASCII code of each char or number
    2. Multiply with 1,11,13,17,3,5,7 (prime numbers) and emphasize on letters rather than numbers, as alphabets (A - Z) have wider range than numbers (0 - 9).
    3. Sum up all digit results from above
    4. Modulo the sum with the number of buckets
    5. (Output:) Return the index of bucket where this plate can be added
    '''
    def __getHashIndex(self, value):
        asciiSum = 0
        weights = [1,11,13,17,3,5,7] # multiply prime numbers with higher weight on ABC 
        for i in range(0, len(value)):
            asciiSum += int(ord(value[i]))*weights[i] # sum of ASCII 
        hashIndex = asciiSum%len(self.buckets) # mod the number of buckets
        return hashIndex
    
    '''Check if rehash is needed and rehash type based on load factor '''    
    def __needReHash(self):
        loadFactor = float(self.keyTotal) / len(self.buckets)
        if loadFactor > 0.75:
            return "increase"
        elif loadFactor < 0.25:
            return "decrease"
        else: 
            return None

    '''Rehash when load factor is larger than 0.75 or less than 0.25'''
    def __reHash(self, typeOfRehash):
        if typeOfRehash == "increase":
            bucketSize2 = len(self.buckets) * 2
        elif typeOfRehash == "decrease":
            bucketSize2 = len(self.buckets) / 2
        else:
            pass
        bucket2 = PlatesHash(bucketSize2)
        for bucket in self.buckets:
            for position in range(0, bucket.getLen()):
                if bucket.getNode(position+1):
                    bucket2.insert(bucket.getNode(position+1).value, False)
        self.buckets = bucket2.getBuckets()
        
        
        
        
""" Generate random plate numbers in California state format: 1ABC234 """
def generateRandomPlateNumber(howMany=10):
    platesList = []
    for number in range(0, howMany):
        plateNumber = ''.join(random.sample(string.digits, 1))
        plateNumber += ''.join(random.sample(string.ascii_letters.upper(), 3))
        plateNumber += ''.join(random.sample(string.digits, 3))
        platesList.append(plateNumber)
    return platesList


""" Main functions """
if __name__ == "__main__":
    platesHash = PlatesHash()
    platesList = generateRandomPlateNumber(howMany=75) # Specify the number of Keys here
    [platesHash.insert(plateNumber) for plateNumber in platesList]
    platesHash.visualizeHash()
    print platesHash.evaluateHashedResult()
    
   
