print("Type amy Keywords from here for make the operation.Keywords like:ONE,TWO")
print("Type ONE for SUM operation")
print("Type TWO for SUB operation")
print("Type THREE for MUL operation")
print("Type FOUR for DIVISION operation")
print("Type FIVE for finding the whole summation between two numbers")
print("Type SIX to find the EVEN numbers between a couple of numbers")
print("Type SEVEN to find the ODD numbers between a couple of numbers")
choice = input()
print("Choose the first number:")
var1 = int(input())
print("Choose the second number:")
var2 = int(input())

mylist = []

def myFunction(choice,var1,var2):

    if choice=='ONE':
        return var1+var2
    elif choice=='TWO':
        return var1-var2
    elif choice=='THREE':
        return var1*var2
    elif choice=='FOUR':
        return var1/var2
    elif choice=='FIVE':
        sum=0
        for i in range(var1,var2):
            sum=sum+i

        return sum

    elif choice=='SIX':
        for x in range(var1,var2):
            if x%2==0:
                mylist.append(x)
        return mylist

    elif choice=='SEVEN':
        for x in range(var1,var2):
            if x%2!=0:
                mylist.append(x)
    return mylist
print("The result for your choice is", myFunction(choice,var1,var2))