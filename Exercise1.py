a = int(input('Enter the number of times : '))
 
def horizontal():
    print(" --- " * (a))
    return  
    
def vertical():
    print("|    " * (a+1))
    return

for n1 in range(1, a+1):
    horizontal()
    vertical() 
