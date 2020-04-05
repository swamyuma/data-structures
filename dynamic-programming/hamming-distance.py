class Solution:

    def decimal_to_binary(self, num, quotient_array):
        
        # raise error
        if num < 0:
            raise ValueError("Input should be an unsigned integer!")
    
        # calcuate
        remainder = num//2
        quotient = num%2    
        
        if num > 1:
            # recursion
            self.decimal_to_binary(remainder, quotient_array)
        
        # accumalte quotient in an array
        quotient_array.append(quotient)
        #return quotient_array
        return "".join([str(ele) for ele in quotient_array])
        
    def hammingDistance(self, x: int, y: int) -> int:
        
        binary_x = self.decimal_to_binary(x,[]).zfill(31)
        binary_y = self.decimal_to_binary(y,[]).zfill(31)
    
        #print(len(binary_x))
        
        num_of_diffs = 0
        
        for ii in range(len(binary_x)):
            print(binary_x[ii] , binary_y[ii] )
            if binary_x[ii] != binary_y[ii]:
                num_of_diffs += 1
        return num_of_diffs