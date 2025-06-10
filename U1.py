#EX2:
def goldilocks_approved(nums):
    maximum = (max(nums))
    minimum = (min(nums))
    for i in nums:
        if i != maximum and i != minimum:
            return i

nums = [1, 2]
#print(goldilocks_approved(nums))

# EX3:
def delete_minimum_elements(hunny_jar_sizes):
    newlist = []
    while hunny_jar_sizes:
        # we are calling min twice every loop we can save it
        #newlist.append(min(hunny_jar_sizes))
        #hunny_jar_sizes.remove(min(hunny_jar_sizes)) 
        smallest = min(hunny_jar_sizes)
        newlist.append(smallest)
        hunny_jar_sizes.remove(smallest)

    return newlist
        
hunny_jar_sizes = [5, 3, 2, 4, 1]
#print(delete_minimum_elements(hunny_jar_sizes))
#[1, 2, 3, 4, 5]
hunny_jar_sizes = [5, 2, 1, 8, 2]
#print(delete_minimum_elements(hunny_jar_sizes))
#[1, 2, 2, 5, 8]

#EX4:
def sum_of_digits(num):
    total = 0 
    while num > 0:#use only positive numbers
        total += num % 10
        num //= 10
    return total
num = 423
#print(sum_of_digits(num))

num = 123456789
#print(sum_of_digits(num))

#EX5:

def final_value_after_operations(operations):
    tigger = 1 # add it in the function scope
    for i in operations:
        if i == "bouncy" or i == "flouncy":
            tigger = tigger + 1
        if i == "trouncy" or i == "pouncy":
            tigger = tigger - 1
    return tigger
operations = ["trouncy", "flouncy", "flouncy"]
#print(final_value_after_operations(operations))
#2
operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))
#4           



def mystery_function(s):
    count = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
    return count
result = mystery_function("AABBAB")
print(result)

def mystery_function(lst, threshold):
    total = 0
    i = 0
    while i < len(lst) and total + lst[i] <= threshold:
        total += lst[i]
        i += 1
    return total 
result = mystery_function([1, 2, 3, 4, 5], 7)
print(result)
        

def reverse_lst(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]  # correct swap
        left += 1
        right -= 1

    return lst
def has_all_unique_characters(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

def find_needle(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
def can_place_flowers(flowerbed, n):
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            # Get neighbors: treat edges as 0
            empty_left = (i == 0 or flowerbed[i - 1] == 0)
            empty_right = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            
            if empty_left and empty_right:
                flowerbed[i] = 1  # plant the flower
                n -= 1            # reduce how many we still need
                if n == 0:
                    return True
    return n <= 0





        
