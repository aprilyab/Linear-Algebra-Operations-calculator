import numpy as np
def addition(matrix1,matrix2):
    return np.subtract(matrix1,matrix2)
def subtracion(matrix1,matrix2):
    return np.add(matrix1,matrix2)
def multiplication(matrix1,matrix2):
    return np.multiply(matrix1,matrix2)
def transpose(matrix1):
    return np.transpose(matrix1)
def Scalar_Multiplication(matrix1,scalar):
    return np.multiply(matrix1,scalar)
def Determinant(matrix1):
    return np.linalg.det(matrix1)
def Inverse(matrix1):
    return np.linalg.inv(matrix1)
def Rank(matrix1):
    return np.linalg.matrix_rank(matrix1)
def Trace(matrix1):
    return np.trace(matrix1)
def Eigenvalues_and_Eigenvectors(matrix1):
    return np.linalg.eig(matrix1)
def Solve_Linear_Equations(matrix1):
    return np.linalg.solve(matrix1)

while True:
    print("choose your wish matrix operation:  ")
    print("""
    ======= MATRIX OPERATIONS MENU =======
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Scalar Multiplication
    5. Transpose 
    6. Determinant (np.linalg.det)
    7. Inverse (np.linalg.inv)
    8. Rank (np.linalg.matrix_rank)
    9. Trace (np.trace)
    10. Eigenvalues & Eigenvectors (np.linalg.eig)
    11. Solve Linear Equations (np.linalg.solve)
    0. Exit
    ======================================
    """)
    operation=int(input("enter your oprration:  "))
    if operation==0:
        print("thank you for using the calculator:    ")
    elif operation==1: 
        rows1 = int(input("Enter number of rows for first matrix: "))  
        cols1 = int(input("Enter number of columns for first matrix: "))  
        print(f"Enter the elements of the first matrix (each row in a new line):")
        matrix1 = np.array([input().split() for _ in range(rows1)], dtype=int)

        rows2 = int(input("Enter number of rows for second matrix: "))  
        cols2 = int(input("Enter number of columns for second matrix: "))  
        print(f"Enter the elements of the second matrix (each row in a new line):")
        matrix2 = np.array([input().split() for _ in range(rows2)], dtype=int)

        print(addition(matrix1,matrix2))
    elif operation==2: 
        rows1 = int(input("Enter number of rows for first matrix: "))  
        cols1 = int(input("Enter number of columns for first matrix: "))  
        print(f"Enter the elements of the first matrix (each row in a new line):")
        matrix1 = np.array([input().split() for _ in range(rows1)], dtype=int)

        rows2 = int(input("Enter number of rows for second matrix: "))  
        cols2 = int(input("Enter number of columns for second matrix: "))  
        print(f"Enter the elements of the second matrix (each row in a new line):")
        matrix2 = np.array([input().split() for _ in range(rows2)], dtype=int)

        print(subtracion(matrix1,matrix2))
    elif operation==3: 
        rows1 = int(input("Enter number of rows for first matrix: "))  
        cols1 = int(input("Enter number of columns for first matrix: "))  
        print(f"Enter the elements of the first matrix (each row in a new line):")
        matrix1 = np.array([input().split() for _ in range(rows1)], dtype=int)

        rows2 = int(input("Enter number of rows for second matrix: "))  
        cols2 = int(input("Enter number of columns for second matrix: "))  
        print(f"Enter the elements of the second matrix (each row in a new line):")
        matrix2 = np.array([input().split() for _ in range(rows2)], dtype=int)

        print(multiplication(matrix1,matrix2)) 
    elif operation==4: 
        rows1 = int(input("Enter number of rows for first matrix: "))  
        cols1 = int(input("Enter number of columns for first matrix: "))  
        print(f"Enter the elements of the first matrix (each row in a new line):")
        matrix1 = np.array([input().split() for _ in range(rows1)], dtype=int)

        Scalar=int(input("enter your oprration:  "))

        print(Scalar_Multiplication(matrix1,Scalar))   
    elif operation==5: 
        rows1 = int(input("Enter number of rows for first matrix: "))  
        cols1 = int(input("Enter number of columns for first matrix: "))  
        print(f"Enter the elements of the first matrix (each row in a new line):")
        matrix1 = np.array([input().split() for _ in range(rows1)], dtype=int)

        print(transpose(matrix1))  
    elif operation==6: 
        rows1 = int(input("Enter number of rows for first matrix: "))  
        cols1 = int(input("Enter number of columns for first matrix: "))  
        print(f"Enter the elements of the first matrix (each row in a new line):")
        matrix1 = np.array([input().split() for _ in range(rows1)], dtype=int)

        print(Determinant(matrix1))
    elif operation==7: 
        rows1 = int(input("Enter number of rows for first matrix: "))  
        cols1 = int(input("Enter number of columns for first matrix: "))  
        print(f"Enter the elements of the first matrix (each row in a new line):")
        matrix1 = np.array([input().split() for _ in range(rows1)], dtype=int)

        print(Inverse(matrix1))  
    elif operation==8: 
        rows1 = int(input("Enter number of rows for first matrix: "))  
        cols1 = int(input("Enter number of columns for first matrix: "))  
        print(f"Enter the elements of the first matrix (each row in a new line):")
        matrix1 = np.array([input().split() for _ in range(rows1)], dtype=int)

        print(Rank(matrix1)) 
    elif operation==9: 
        rows1 = int(input("Enter number of rows for first matrix: "))  
        cols1 = int(input("Enter number of columns for first matrix: "))  
        print(f"Enter the elements of the first matrix (each row in a new line):")
        matrix1 = np.array([input().split() for _ in range(rows1)], dtype=int)

        print(Trace(matrix1)) 
    elif operation==10: 
        rows1 = int(input("Enter number of rows for first matrix: "))  
        cols1 = int(input("Enter number of columns for first matrix: "))  
        print(f"Enter the elements of the first matrix (each row in a new line):")
        matrix1 = np.array([input().split() for _ in range(rows1)], dtype=int)

        print(Eigenvalues_and_Eigenvectors(matrix1))
    elif operation==11: 
        rows1 = int(input("Enter number of rows for first matrix: "))  
        cols1 = int(input("Enter number of columns for first matrix: "))  
        print(f"Enter the elements of the first matrix (each row in a new line):")
        matrix1 = np.array([input().split() for _ in range(rows1)], dtype=int)

        print(Solve_Linear_Equations(matrix1))
    else:
        print("Invalid choice! Please select a valid option.")




