# Matrix Operations Project

This is a Python-based program that allows users to perform various matrix operations using the NumPy library. The program offers a simple menu-driven interface where users can select different operations to perform on matrices.

## Features

The program supports the following matrix operations:
- **Addition**
- **Subtraction**
- **Multiplication**
- **Scalar Multiplication**
- **Transpose**
- **Determinant**
- **Inverse**
- **Rank**
- **Trace**
- **Eigenvalues and Eigenvectors**
- **Solving Linear Equations**

## Requirements

- Python 3.x
- NumPy Library (You can install it via `pip install numpy`)

## How to Use

1. **Start the program**:
   - Run the Python script.
   
2. **Select an operation**:
   - The program will display a menu of available matrix operations.
   - Enter the number corresponding to the operation you want to perform.
   
3. **Enter the matrix dimensions**:
   - For most operations, you will be asked to input the dimensions of the matrices (rows and columns).
   - You will then input the matrix elements, one row at a time, separated by spaces.

4. **Perform the operation**:
   - The program will compute and display the result of the selected matrix operation.
   
5. **Repeat or Exit**:
   - After completing an operation, you can choose to perform another one or exit the program.

### Example Operation

#### 1. **Matrix Addition**
   - Enter the dimensions of two matrices.
   - Enter the elements of both matrices.
   - The program will output the result of the addition of the two matrices.

#### 2. **Solving Linear Equations**
   - If solving a system of linear equations, input the matrix for the coefficients and the right-hand side vector.

## Operations Menu

1. **Addition**: Adds two matrices.
2. **Subtraction**: Subtracts the second matrix from the first.
3. **Multiplication**: Multiplies two matrices.
4. **Scalar Multiplication**: Multiplies a matrix by a scalar.
5. **Transpose**: Transposes a matrix.
6. **Determinant**: Computes the determinant of a matrix.
7. **Inverse**: Computes the inverse of a matrix.
8. **Rank**: Computes the rank of a matrix.
9. **Trace**: Computes the trace of a matrix.
10. **Eigenvalues & Eigenvectors**: Computes eigenvalues and eigenvectors of a matrix.
11. **Solve Linear Equations**: Solves a system of linear equations using matrix equations.

## Example Use Case

1. Choose the operation: **1** (Addition)
2. Enter the dimensions for two 2x2 matrices.
3. Input the matrix elements.
4. The program will return the sum of the two matrices.

## Error Handling

- The program checks for common input errors, such as mismatched matrix dimensions, and will prompt you to enter correct values.
- For matrix inversion and other operations that may not be possible (e.g., singular matrices), the program will handle errors appropriately.

## License

This project is open-source and available for modification and redistribution under the MIT License.

## Contributing

Contributions are welcome! If you have any improvements or bug fixes, please feel free to fork the repository and submit a pull request.

## Contact

For any questions or feedback, please contact the project maintainer at henokapril@gmail.com .
