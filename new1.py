text = "hello hi" 
v=0
c=0
for ch in text:
    if ch.lower() in "aeiou":
        v += 1
    elif ch.isalpha():
        c += 1

print("vowels:",v)
print("consonants:",c)  



def sum_n(n):
    if n==1:
        return 1
    return n + sum_n(n-1)
n=7
print("sum:",sum_n(n))


def count_case(text):
    upper=0
    lower=0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1


    print("Uppercase:",upper)
    print("Lowercase:",lower)
count_case("HDUHFIUHUFIuhfgohfghfuohguofgIJFIOH")                



def fibonacci(n):
    a, b = 0, 1
    result = []

    for i in range(n):
        result.append(a)
        a, b =b, a + b
    return result
print(fibonacci(9))

def is_armstrong(num):
    s = str(num)
    power = len(s)
    total = 0

    for digit in s:
        total += int(digit) ** power

    if total == num:
        print("Armstrong number")  
    else:
        print("Not armstrong")

is_armstrong(162) 


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(80))


def merge(a,b):
    return list(set(a+b))
list1 = [1,3,4,6]
list2 = [9,2,4,4,7]
print(merge(list1,list2))

def sort(arr):
    n = len (arr)

    for i in range(n):
        for j in range(0,n - i -1):
            if arr [j]> arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1],arr[j]
                return arr
print(sort([2,3,2,4,8,1]))

def secondlarge(lst):
    lst= list(set(lst))
    lst.sort()
    return lst[-2]
print (secondlarge([64,77,88,880.28]))


def removedupli(lst):
    return list (set(lst))
print(removedupli([2,3,2,34,4,5,6,7]))


def find_max_min(lst):
    largest = lst[0]
    smallest = lst[0]

    for num in lst:
        if num >largest:
            largest = num
        if num < smallest:
            smallest = num

            print("Largest:", largest) 
            print("Smallest:", smallest)
find_max_min([29,19,36,367])              
                

def removedupli(s):
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result
print(removedupli("programmin"))        


def revestring(s):
    result = ""
    for char in s:
        result = char + result
    return result
print (revestring("hello there"))    


def frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq [char]+=1
        else:
            freq[char]=1
    return freq 
print(frequency("hello"))


def palindrome(s):
    left, right =0,len(s)-1
    while left<right:
        if s [left]!= s[right]:
            return False
        left += 1
        right -= 1
    return True
print (palindrome("madam"))
print(palindrome("hi"))    


