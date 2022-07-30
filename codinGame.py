## The same letters of two strings
def countLetters():
    string1 = input("Enter str 1 : ")
    string2 = input("Enter str 2 : ")

    s1 = set(string1)
    s2 = set(string2)

    print(s1.intersection(s2))

## Count frequency 
# Sheena loves apple, her sister loves orange
def countFrequency():
    text = input("Enter the text")
    txt = text.split(' ')
    
    count_freq = {}
    for t in txt:
        if t not in count_freq.keys():
            count_freq[t] = 0
        count_freq[t] += 1
    print(count_freq)

# lists to dictionary
def lists_to_dict():
    list1 = ["hamza", "jad", "jack"]
    list2 = [5, 10, 2]
    print(dict(zip(list1, list2)))

# Find missing number 
def findMissing(list1):
    s = (list1[0] + list1[-1]) * list1[-1] / 2
    print(s - sum(list1))

# Find maximum consecutive elements
def maxSum(arr, K):
    maxSum = -100
    for i in range(len(arr) - K + 1): 
        sum = 0
        for k in range(K):
            sum += arr[k + i]
        maxSum = max(maxSum, sum) 
    return maxSum

def maxSum2(arr, sw_size):
    maxSum = sum([arr[i] for i in range (sw_size)])
    for i in range (len(arr) - sw_size):
        s = maxSum - arr[i] + arr[i + sw_size]
        maxSum = max(maxSum, s)
    return maxSum

print(maxSum2([1, 2, 3, 4, 4, 5, 8], 2))

