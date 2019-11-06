# Recursive program to reverse a String 

def rec_reverse(str) :
    if(len(str)==1) :
        return str
    else :
        return  rec_reverse(str[1:]) + str[0] ; 


mystr=input(' Enter any String :: ')
print('REVERSE String is :: ' + rec_reverse(mystr))
