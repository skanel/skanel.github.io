---
layout: post
title: Blockchain|ងាយយល់អំពី Blockchain
---

Blockchain គឺដូចគ្នា​នឹងLinked List data structure ដែលតភ្ជាប់គ្នាពីមួយទៅមួយឥតដាច់ ដូចទៅនឹងច្រវ៉ាក់កង់ដែល​យើងស្គាល់។
អ្នកអាចចាប់ផ្ដើមមាន​គំនិតខ្លះៗដោយអានកូដខាងក្រោមនេះ៖<br/>
![_config.yml]({{ site.baseurl }}/images/block.png)<br/>

```python
element1 = input("Give the first element of the blockchain ")
blockchain = [element1]
def add_list():
   blockchain.append([blockchain[-1], 3.2])
   print(blockchain)

add_list()
add_list()
add_list()
```

យើងបន្ថែមកូដខាងលើ​ដើម្បីអោយប្រសើរឡើង

```python
blockchain = [] # Global variable
def get_last_blockchain_value():
    return blockchain[-1]
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_blockchain_value, transaction_amount])

def get_user_input():
    return float(input("Input transaction amount please: '))

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount =  get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount =  get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)
```
ពេលរត់វានឹងបង្ហាញស្រដៀងនេះ អាស្រ័យលើការញ្ចូល៖ <br/>
![_config.yml]({{ site.baseurl }}/images/trx.png)

# តើវាតភ្ជាប់គ្នា​ដោយរបៀបណា <br>
![_config.yml]({{ site.baseurl }}/images/bc.png)
