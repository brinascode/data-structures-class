# def checkEquality(string): #hannah 
#     index_last = len(string) - 1
#     index_first = len(string) - index_last
#     if string[index_first] == string[index_last]:
#         return True
#     else:
#         return False
    
# def isPalindrome(string):
#     if string
    
    
# def checkEquality(string,index_last): #hanonah 
#     length = len(string)
#     index_last = len(string) - 1
#     index_first = 0
#     position = 1
    
#     # Odd string lengths: o
#     if index_last == index_first:
#         return True
#     else:
#         checkEquality(string,index_last-1)
    
#     # Even string lengths --> find a way to make them odd (maybe add something in the middle?)
    
#     if (string[index_first] == string[index_last]) & position =   :
#         return True
#     else:
#         return False
    
def checkerOld(string):
    # Base case: if we have one letter --> return true
    last_index = len(string)-1
    if len(string) == 1:
        return True #length of the empty string is 0
    else:
        if string[0] == string[last_index]: # What it's doing --> base function
            return True and checker(string)
        else:
            return False and checker(string)
        
def checker(string):
    # Base case: if we have one letter --> return true
    print(string)
    if len(string) <= 1:
        return True #length of the empty string is 0
    else:
        if string[0] == string[-1]: # What it's doing --> base function
            checker_result=checker(string[1:-1])
            print(f'{string} result: {checker_result}')
            return checker_result
        else:
            return False       
        
        
print(checker("hanplnah"))
        
        
 # You can break a recursion outside a base case if there's no reason to continue   
        
#You want a smaller problem each time,  so that anytime it calls itself it's searching a smaller space.
#Shrink the search space
#hannah, anna, nn
# checker(string[1:-1])
# def checker (string,start,end)
# checker ('hannah',0,-1)


#Before we return anything, we execute the function on a smaller space
#You're not getting anything back, until you're all the way down
