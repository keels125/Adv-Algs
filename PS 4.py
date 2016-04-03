#Keely Hicks
#Keely Hicks
#CS 355
#Problem Set 4

def SCS():
    #get the strings from user
    str1=input("Please enter the first string: ")
    str2=input("Please enter the second string: ")

    m=len(str1) #use lengths to create DP array
    n=len(str2)
   
    scs=[[0 for x in range(n+1)] for x in range(m+1)] #create DP array


    #base cases
    for i in range(0, m+1):
        for j in range(0, n+1):
            if (i==0):
                scs[i][j]=j
            elif (j==0):
                scs[i][j]=i

    #recursive cases
    for i in range(1, m+1):
        for j in range(1, n+1):
            
            if (str1[i-1]==str2[j-1]):
                scs[i][j]=scs[i-1][j-1]+1
                
            else:
                scs[i][j]=min((scs[i][j-1]+1), (scs[i-1][j]+1))
   
    
    return scs[m][n] #return last item = SCS length        
                

def main():
    print("The SCS of the two strings is: ", SCS())

main()
