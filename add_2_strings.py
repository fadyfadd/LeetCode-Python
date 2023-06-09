def add_2_strings(nbr1  , nbr2 ):
        stk = list()
        value = ""
        retain=0
         
        l=max(len(nbr1) , len(nbr2))
        nbr1 = nbr1.rjust(l , '0')
        nbr2 = nbr2.rjust(l, '0')

        for i in range(len(nbr1) - 1, -1 , -1):
            sum=int(nbr1[i:i+1]) + int(nbr2[i:i+1]) + retain
            if (sum < 10):
                stk.append(sum)
                retain = 0
            else:
                stk.append(str(sum)[1:2])
                retain = 1

        if (retain == 1):
            stk.append(1)

        while (len(stk) != 0):
            value = value + str(stk.pop())


        return value


print(add_2_strings("9" , "1")) #10
print(add_2_strings("9" , "101")) #110
print(add_2_strings("99" , "2")) #101