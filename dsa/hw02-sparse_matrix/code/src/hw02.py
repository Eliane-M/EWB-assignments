from pathlib import Path

base_dir = Path(__file__).parent.parent.parent

matrix1 = base_dir / "sample_inputs" / "matrixfile1.txt"
matrix2 = base_dir / "sample_inputs" / "matrixfile3.txt"


def load_sparse_matrix(matrix):
    try:
        with open(matrix, 'r') as f:
            rows = int(f.readline().strip().split('=')[1])
            cols = int(f.readline().strip().split('=')[1])
            matrix = {}
            
            for line in f:
                # Strip leading/trailing spaces and check parentheses
                stripped_line = line.strip()
                if not stripped_line.startswith('(') or not stripped_line.endswith(')'):
                    raise ValueError("Input file has wrong format")
                
                try:
                    # Remove parentheses and split by commas
                    cleaned_line = stripped_line.strip('()')
                    r, c, v = cleaned_line.split(',')
                    
                    # Check for integer values (no floating point values allowed)
                    r, c, v = int(r), int(c), int(v)
                except ValueError:
                    raise ValueError("Input file has wrong format")

                # Store the value in the matrix dictionary
                matrix[(r, c)] = v
        
        return matrix, rows, cols
    except FileNotFoundError:
        print(f"Error: File '{matrix}' not found.")
        return None, None, None
    except Exception as e:
        print(f"Error loading matrix from {matrix}: {str(e)}")
        return None, None, None


def multiply_sparse_matrices(mat1, mat2, rows1, cols1, rows2, cols2):
    if None in (mat1, mat2, rows1, cols1, rows2, cols2):
        print("Error: Invalid matrix data")
        return None
    if cols1 != rows2:
        print("Error: Matrices must have compatible dimensions for multiplication.")
        return None
    
    result = {}

    mat2_transposed = {}
    for (r, c), v in mat2.items():
        if c not in mat2_transposed:
            mat2_transposed[c] = {}
        mat2_transposed[c][r] = v
    
    for (r1, c1), v1 in mat1.items():
        for (r2, c2), v2 in mat2.items():
            if c1 == r2:
                if (r1, c2) in result:
                    result[(r1, c2)] += v1 * v2
                else:
                    result[(r1, c2)] = v1 * v2
                    
    return result

def add_sparse_matrices(mat1, mat2, rows1, cols1, rows2, cols2):
    if rows1 != rows2 or cols1 != cols2:
        print("Error: Matrices must have the same dimensions for addition.")
        return None
    
    result = mat1.copy()
    for (r, c), v in mat2.items():
        if (r, c) in result:
            result[(r, c)] += v
        else:
            result[(r, c)] = v
    
    return result

def subtract_sparse_matrices(mat1, mat2, rows1, cols1, rows2, cols2):
    if rows1 != rows2 or cols1 != cols2:
        print("Error: Matrices must have the same dimensions for subtraction.")
        return None
    
    result = mat1.copy()
    for (r, c), v in mat2.items():
        if (r, c) in result:
            result[(r, c)] -= v
        else:
            result[(r, c)] = -v
    
    return result

def print_sparse_matrix(matrix, rows, cols):
    if matrix is None or rows is None or cols is None:
        print("Cannot print invalid matrix")
        return
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(str(matrix.get((r, c), 0)))
        print(' '.join(row))

# Main execution
def main():
    # Load matrices
    print(f"Loading matrix 1 from {matrix1}")
    mat1, rows1, cols1 = load_sparse_matrix(matrix1)
    if mat1 is not None:
        print(f"Matrix 1 dimensions: {rows1}x{cols1}")
    
    print(f"\nLoading matrix 2 from {matrix2}")
    mat2, rows2, cols2 = load_sparse_matrix(matrix2)
    if mat2 is not None:
        print(f"Matrix 2 dimensions: {rows2}x{cols2}")
    
    # Perform operations
    sum_result = add_sparse_matrices(mat1, mat2, rows1, cols1, rows2, cols2)
    diff_result = subtract_sparse_matrices(mat1, mat2, rows1, cols1, rows2, cols2)
    prod_result = multiply_sparse_matrices(mat1, mat2, rows1, cols1, rows2, cols2)
    
    # Print results
    print("Sum of matrices:")
    if sum_result:
        print_sparse_matrix(sum_result, rows1, cols1)
    # else:
    #     print('Could not find sum of matrices')
    
    print("\nDifference of matrices:")
    if diff_result:
        print_sparse_matrix(diff_result, rows1, cols1)
    # else:
    #     print('Could not find difference of matrices')
    
    print("\nProduct of matrices:")
    if prod_result:
        print_sparse_matrix(prod_result, rows1, cols2)

if __name__ == "__main__":
    main()