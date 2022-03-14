def solution(A):
    waysToCut = 0
    ## begin solution by checking if garden is already aesthetically pleasing
    if isAesthetic(A):
        return 0
    
    for i in range(len(A)):
        ## creating subarrays that excludes current iter of tree
        a = [j for j in A]
        del a[i]
        ## check if subarray is aesthetically pleasing
        if isAesthetic(a):
            waysToCut += 1 ## increment ways to cut if true
    if waysToCut == 0:
        return -1
    return waysToCut


def isAesthetic(a):
    for i in range(1,len(a)-1):
        ## check if current iter tree alternate compared to the previous and next iter
        if (a[i] >= a[i-1] and a[i+1] >= a[i]) or (a[i] <= a[i-1] and a[i+1] <= a[i]):
            return False
    return True
    
