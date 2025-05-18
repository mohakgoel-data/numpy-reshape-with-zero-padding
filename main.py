# -----------------------------
# Reshape Helper with Zero Padding
# Author: [Your Name]
# Description:
#     Takes user input to build a 1D NumPy array,
#     lets user reshape it with custom rows and columns,
#     and auto-fills remaining elements with zeros if needed.
# -----------------------------
import numpy as np


arr=np.array([])  
size = int(input("Enter the number of elements you wanna add in the array: "))

for i in range (0,size):
    match i:
        case 0:
            num = int(input(f"Enter the 1st number: "))
        case 1:
            num = int(input(f"Enter the 2nd number: "))
        case _:
            num = int(input(f"Enter the {i+1}th number: "))

    arr=np.append(arr,num)

def rowCon(): #Asks the user for row count and ensures it’s valid for reshaping.
    rows = int(input("Enter the number of rows you want it to have: "))
    if size/rows >=1:
        return rows

    else:
        print(f"{rows} cant fit all the elements, try again!")
        return rowCon()

def colCon(r): #Asks and suggests the user the column count and tells if it is gonna have empty spaces
    for i in range(1,int((size/r)+1)):
        if (size%i)==0:
            perfectCol = i
    if (str(size/r)).endswith(".0"):
        col = int(input(f"Perfect column count is {perfectCol}, still enter your desired number: "))
    else:
        col = int(input(f"(We will fill the missing column places with zeros)\nEnter your desired column count:"))
        
    return col

def runCheck(r,c): #Checks if all the arguments are good to go noting that program only adds zeros if the last row has empty spaces.
    if size>((r-1)*c):
        return r,c
    else:
        print(f"Making the array is not possible with {r} rows and {c} columns.")
        r = rowCon()
        c = colCon(r)
        return runCheck(r,c)
    
def makeArray(r,c,ar=arr): #Does the final task of reshaping and printing the array.
    zerosReq=(r*c)-size
    ar=np.append(ar,np.zeros(zerosReq))
    ar=ar.reshape(r,c)
    print(f"The final array looks like:\n{ar}")
    print(f"with the shape as:\t{ar.shape}")

r = rowCon()
c = colCon(r)
rows , cols = runCheck(r,c)
makeArray(rows, cols)        
