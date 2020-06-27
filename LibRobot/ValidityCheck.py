def vCheck(ISBN):
    
    def boolean(ISBN):
        if len(ISBN) !=  10:
            return False

        sum1  = 0
        for i in range(len(ISBN)-1):
            if int(ISBN[i]) not in range(10):
                return False

            else:
                sum1  += int(ISBN[i]) * (10 - i) 

        if ISBN[9] != 'X' and int(ISBN[9]) not in range(10):
            return False
    
        else:
            if ISBN[9] == 'X':
                sum1 += 10
            
            else:
                sum1 += int(ISBN[9])

        if sum1 % 11 == 0:
            return True

        else:
            return False

    if boolean(ISBN):
        return True
    
    else:
        return False
