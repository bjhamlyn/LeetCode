"""
This function checks to see if a given integer 'x', is a palindrome. The function returns
True if the integer is a palindrome, and False otherwise. 
"""

def is_palindrome(x): 
    s = str(x) #convert the integer x to a string and assign the variable s 
    n = len(s) #get the length of the string 's' using the len function and assign the variable n
    for i in range(n // 2): #divide the string in half using the range function
        if s[i] != s[n -i -1]: #check whether character at i == the character at the opposite end
            # i.e. does index 0 == index -1, etc...
            return False #if the characters do not match, end the function and return False
    return True #if the loop completes without returnng False, the the string is a palindrome, return True


"""
Several test integers and their print commands. They can be removed if completing on a site such as 
leet code, or hacker rank, etc.
"""
x = 12345678987654321
result = is_palindrome(x)
print(result)

x = 23149812946987321469
result = is_palindrome(x)
print(result)

x = 11
result = is_palindrome(x)
print(result)