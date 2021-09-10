def classify_triangle(a,b,c):
    #inputs should all be numbers, and therefore not of type 'str'
    triangles = ['Equilateral triangle', 'Isosceles triangle', 'Scalene triangle', 'Right triangle', 'Invalid triangle']
    intA = int(a)
    intB = int(b)
    intC = int(c)
    #check if valid triangle first! If all three are true, then proceed to classify
    checkOne = (intA + intB > intC) 
    checkTwo = (intA + intC > intB)
    checkThree = (intB + intC > intA)

    if(not(checkOne and checkTwo and checkThree)):
        return(triangles[4])
        
    #equilateral triangle test
    if(intA == intB == intC):
        return(triangles[0])
    #Isosceles triangle test
    elif(intA == intB and (intA != intC) and (intB != intC)):
        #Some isosceles can be right triangles! Check for right triangle.
        if(intA**2 + intB**2 == intC**2):
            return(triangles[3] + "and " + triangles[1])
        return triangles[1]
    #Scalene triangle test
    elif(intA != intB != intC):
        #Some scelene can be right triangles! Check for right triangle.
        if(intA**2 + intB**2 == intC**2):
            return(triangles[3] + " and " + triangles[2])
        return triangles[2]
    #Right triangle test
    elif(intA**2 + intB**2 == intC**2):
        return(triangles[3])
        

def get_input(side_number):
    triangle_sides = ["Side 1: ", "Side 2: ", "Hypotenuse: "]
    user_input = input("Enter value of " + triangle_sides[side_number])
    if(user_input.isdigit() and int(user_input) > 0):
        return user_input
    else:
        print("Invalid input, please enter a number greater than 0... \n")
        return get_input(side_number)


#"Main" Routine
# print("Enter three values of the lengths of a triangle to get its classification back! \n")
# first = get_input(0)
# second = get_input(1)
# third = get_input(2)
# classify_triangle(first, second, third)

#print(classify_triangle(first, second, third))

if __name__ == '__main__':
    # examples of running the code
    classify_triangle(1,2,3)
    classify_triangle(1,1,1)
