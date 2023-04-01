"""
I came up with a better version of the code that we worked on with Ethan 
earlier today. It was the twoSum problem where, given an array of integers, 
and a target integer value, we needed to determine which pair of integers 
within the array added up to the target value and return the index of those 
integer values.

The solution I came up with 
"""


class Solution(object): #line provided in leet code start 

    def twoSum(self, nums, target): #code provided in leet code start

        my_dict = {} #initialize an empty dictionary

        for i, num in enumerate(nums): #here we enumerate through the array. i 
            #represents the index of our current position and num represents the 
            # #value of our current integer 

            x = target - num #this is pretty much what we did earlier today. 
            #Subtract the current value from the target value and assign it to 
            # #the variable x.

            if x is my_dict: #check to see if the current value is in the dictionary 
                #(seems a lot easier than how we did it earlier today)

                return [my_dict[x], i] # return the x value and index

            my_dict[num] = i  #if x is not in my_dict, we add the current value 
            #(num)and its index to my_dict.

        return [] #returns an empty list if no two integer values add up to the target. 
    #We could easily change this to (return -1), or to a print statement, etc.