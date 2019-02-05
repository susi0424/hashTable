# HashTable #

Considering the HyreCar business background information, this hash table is designed for car plates for fast searching, storing, and retrieving. And it is dynamic, triggering rehash based on load factor changes.

Implemented HashTable in Python using data structures __List(array)__ and __LinkedList__ for resolving collisions, combined advantages from both:
- List(array): Easy Search.
- LinkedList: Easy Insert/Delete.


#### Highlights ####
  - Always __add new node at the head of LinkedList__, so the insert function takes only O(1) time complexity, and no need to traverse the LinkedList.
  - Using __Standard Deviation to evaluate the distribution of LinkedLists__. In most cases, the lengths of LinkedLists are between 0 and 3. 
  - __Rehash the hash table dynamically based on Load Factor__, (trigger rehash by any Insert or Delete causing Load Factor larger than 0.75 or smaller than 0.25). The Rehash function is also object-oriented.
----
#### Hash Function ####
function name: __getHashIndex()
*Input* :  A plate - assume California format (eg:1ABC234)
1. Get ASCII code of each char or number.
2. Multiply with 1,11,13,17,3,5,7 (prime numbers) and emphasize on letters rather than numbers, as alphabets (A - Z) have wider range than numbers (0 - 9).
3. Sum up all digit results from above.
4. Modulo the sum with the number of buckets.

*Output* : Return the index of bucket where this plate can be added

#### HashTable Class (PlatesHash) ####
(This table excludes methods/functions for testing purpose)

Method  | Purpose
------------- | -------------
__ init()__  | Initialize a hash table with a given bucket size
insert()  | Insert a plate (numbers) into a bucket (list) as a LinkedList node
delete()  | Delete a plate from the bucket
search()  | Check if a specific plate exists in any bucket
getBuckets()  | Get all buckets
__get()  | Get the LinkedList from a bucket
__getHashIndex()  | Hash function: get the index of bucket where this plate can be added
__needReHash()  | Check if rehash is needed and rehash type based on load factor
__reHash()  | Rehash when load factor is larger than 0.75 or less than 0.25


#### Methods/Functions for Testing Purpose ####
- generateRandomPlateNumber()
    > Generate random plate numbers in California state format "1ABC234", and you can specify the number of keys by passing a specific value for parameter howMany (default value is 10 if not assigned).
- visualizeHash()
    > Print out the result of the whole hash table.
- evaluateHashedResult()
    > Get the Standard Deviation of all LinkedList lengths, for evaluating the results distribution.

#### Usage ####
1. Clone the repo to your machine.

`$ git clone https://github.com/susi0424/hashTable.git`

2. Excute the script

`$ python hashTable.py`

3. See the result

