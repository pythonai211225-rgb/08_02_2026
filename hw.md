# Python – Lists & Strings Exercises (with Solutions)

## 1. Remove items from one list based on another

**Task**
Remove all items from `list1` that appear in `list2`
Print `list1` at the end

```python
list1 = [1, 3, 5, 1, 7, 9, 2, 2, 8, 5, 10, 5]
list2 = [1, 2, 5]

for item in list2:
    while item in list1:
        list1.remove(item)

print(list1)
```

## 2. Merge three lists using loops only

**Task**
Create `list4` that contains all values from `list1`, `list2`, and `list3`
Use loops only (no `+`)

```python
list1 = [1, 2, 9, 88, 0]
list2 = [3, 4, -3]
list3 = [5, 6, 55]

list4 = []

for item in list1:
    list4.append(item)
for item in list2:
    list4.append(item)
for item in list3:
    list4.append(item)

print(list4)
```

## 3. Items in list1 that do NOT appear in list2

```python
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4]

list3 = []
for item in list1:
    if item not in list2:
        list3.append(item)

print(list3)
```

## 4. Items that appear in both lists (no duplicates)

```python
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6, 7]

list3 = []
for item in list1:
    if item in list2:
        list3.append(item)

print(list3)
```

## 5. Remove from list1 all items that appear in list2 or list3

```python
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [2, 4]
list3 = [5, 6]
```

**Result:**

```
[1, 3, 7]
```

python
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [2, 4]
list3 = [5, 6]

````

## 6. BONUS – Merge two sorted lists into a sorted list

```python
list1 = [1, 4, 6]
list2 = [2, 5, 7]
````

**Result:**

```
[1, 2, 4, 5, 6, 7]
```

python
list1 = [1, 4, 6]
list2 = [2, 5, 7]

````

## 7. Count items from list1 that appear in list2

```python
list1 = [1, 2, 3, 4, 5, 2, 2]
list2 = [2, 4]
````

**Result:**

```
4
```

python
list1 = [1, 2, 3, 4, 5, 2, 2]
list2 = [2, 4]

## 8. Remove names by blacklist

```python
names = ["danny", "moshe", "suzi", "sharon", "avi"]
blacklist = ["moshe", "avi"]
````

**Result:**

```
["danny", "suzi", "sharon"]
```

python
names = ["danny", "moshe", "suzi", "sharon", "avi"]
blacklist = ["moshe", "avi"]

## 9. Separate even and odd numbers

```python
list1 = [1, 2, 3, 4, 5, 6, 7]
````

**Result:**

```
list_even = [2, 4, 6]
list_odd = [1, 3, 5, 7]
```

python
list1 = [1, 2, 3, 4, 5, 6, 7]

## 10. Copy only ALL-uppercase strings

```python
list1 = ["HELLO", "World", "PYTHON", "code", "TEST"]
````

**Result:**

```
["HELLO", "PYTHON", "TEST"]
```

python
list1 = ["HELLO", "World", "PYTHON", "code", "TEST"]

## 11. Copy strings that start with a capital letter

```python
list1 = ["Hello", "world", "Python", "java", "Code"]
````

**Result:**

```
["Hello", "Python", "Code"]
```

python
list1 = ["Hello", "world", "Python", "java", "Code"]

## 12. Split sentences into words

```python
sentences = [
    "Hello world",
    "Python is fun",
    "I love coding"
]
````

**Result:**

```
["Hello", "world", "Python", "is", "fun", "I", "love", "coding"]
```

python
sentences = [
"Hello world",
"Python is fun",
"I love coding"
]

````

## 13. Strip spaces and ignore empty strings

```python
list1 = ["  hello  ", "   ", "python", "  code ", ""]
````

**Result:**

```
["hello", "python", "code"]
```

python
list1 = ["  hello  ", "   ", "python", "  code ", ""]

````

## 14. Replace letters in all strings

```python
list1 = ["hello", "world", "python"]
````

**Result:**

```
["hell0", "w0rld", "pyth0n"]
```

python
list1 = ["hello", "world", "python"]

````

## 15. Count strings that end with a specific word

```python
list1 = ["good morning", "morning sun", "happy morning", "good night"]
````

**Result:**

```
2
```

python
list1 = ["good morning", "morning sun", "happy morning", "good night"]

````

## 16. Separate numeric, text, and mixed strings

```python
list1 = ["123", "hello", "42", "F114", "python", "007", "A14"]
````

**Result:**

```
numbers = ["123", "42", "007"]
texts = ["hello", "python"]
mixed = ["F114", "A14"]
```

python
list1 = ["123", "hello", "42", "F114", "python", "007", "A14"]

````

## 17. Reverse only uppercase words

```python
list1 = ["HELLO", "World", "PYTHON", "code"]
````

**Result:**

```
["OLLEH", "World", "NOHTYP", "code"]
```

python
list1 = ["HELLO", "World", "PYTHON", "code"]

```
```
