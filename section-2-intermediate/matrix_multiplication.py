# 2x2 matrix multiplication without numpy
def multiply_matrix(A,B):
    return [[sum(a*b for a,b in zip(row_a,col_b))
             for col_b in zip(*B)]
             for row_a in A]
X = [[int(input("Enter number x11: ")),int(input("Enter number x12: "))],
     [int(input("Enter number x21: ")),int(input("Enter number x22: "))]]
Y = [[int(input("Enter number y11: ")),int(input("Enter number y12: "))],
    [int(input("Enter number y21: ")),int(input("Enter number y22: "))]]
print(f"The multiplication of matrices {X}X{Y} = {multiply_matrix(X,Y)}")