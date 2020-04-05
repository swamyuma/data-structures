class Solution:

    '''
    https://en.wikipedia.org/wiki/Hamming_distance
    '''
    def decimal_to_binary(self, num, remainder_array):
        
        '''
        Method: successive divison method to convert decimal to binary
        Example: 5//2= 2 (remainder 1)  /|\ (Least significant bit)
                 2//2= 1 (remainder 0)   |
                 1//2= 0.5 (remainder 1) |  (Most significant bit) 
        Answer: decimal_to_binery(5) = 101
        '''
        # raise error
        if num < 0:
            raise ValueError("Input should be an unsigned integer!")
    
        # calcuate
        quotient = num//2
        remainder = num%2    
        
        if num > 1:
            # recursion
            self.decimal_to_binary(quotient, remainder_array)
        
        # accumalte remainder in an array
        remainder_array.append(remainder)
        
        #return remainder_array
        return "".join([str(ele) for ele in remainder_array])
        
    def hammingDistance(self, x: int, y: int) -> int:
        
        # Adding a zfill of 31 to have test cases ranging upto 2^31
        binary_x = self.decimal_to_binary(x,[]).zfill(31)
        binary_y = self.decimal_to_binary(y,[]).zfill(31)
    
        #print(len(binary_x))
        
        num_of_diffs = 0
        
        for ii in range(len(binary_x)):
            print(binary_x[ii] , binary_y[ii] )
            if binary_x[ii] != binary_y[ii]:
                num_of_diffs += 1
        return num_of_diffs

## Leetcode
'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''
