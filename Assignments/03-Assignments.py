# Linear Algebra and Matrix Theory

# QS.1 - Define a linear transformation. Show whether the function T(x, y) = (2x, 3y) is a linear transformation by checking the two required properties.

# Here;

# A linear transformation is a function in linear algebra that maps vectors from one vector to another while preserving the operations of vector addition and scalar multiplication.

import numpy as np

# Define T(x, y) = (2x, 3y)

def T(v):
    return np.array([2 * v[0], 3 * v[1]])

# Test additivity
u = np.array([0, 2])
v = np.array([3, 4])
left = T(u + v)
right = T(u) + T(v)
print("Additivity:", np.allclose(left, right))

#Output - Additivity: True

# Test homogeneity
c = 2
left = T(c * u)
right = c * T(u)
print("Homogeneity:", np.allclose(left, right))

#Output - Homogeneity: True

# QS.2 - Write a NumPy function that checks if a given transformation matrix satisfies additivity and scalar multiplication preservation (i.e., linearity).


def is_linear_transformation(A, tol=1e-10):
    """
    Check if a given matrix A represents a linear transformation.
    Tests additivity: T(u + v) = T(u) + T(v)
    and homogeneity: T(c * u) = c * T(u)
    
    Parameters:
    A : numpy.ndarray
        The transformation matrix (m x n)
    tol : float
        Tolerance for floating-point comparison
    
    Returns:
    bool : True if A satisfies linearity properties, False otherwise
    """
    # Get dimensions of A
    m, n = A.shape
    
    # Generate random vectors u and v in R^n
    u = np.random.rand(n)
    v = np.random.rand(n)
    
    # Generate a random scalar
    c = np.random.rand()
    
    # Test additivity: T(u + v) == T(u) + T(v)
    T_u_plus_v = A @ (u + v)  # T(u + v)
    T_u_plus_T_v = (A @ u) + (A @ v)  # T(u) + T(v)
    additivity_check = np.allclose(T_u_plus_v, T_u_plus_T_v, rtol=0, atol=tol)
    
    # Test homogeneity: T(c * u) == c * T(u)
    T_cu = A @ (c * u)  # T(c * u)
    c_Tu = c * (A @ u)  # c * T(u)
    homogeneity_check = np.allclose(T_cu, c_Tu, rtol=0, atol=tol)
    
    return additivity_check and homogeneity_check

# Example usage
if __name__ == "__main__":
    # Example 1: Linear transformation (scaling)
    A = np.array([[2, 0], [0, 3]])  # T(x, y) = (2x, 3y)
    print("Matrix A:\n", A)
    print("Is linear transformation:", is_linear_transformation(A))  # Should print True
    
    # Example 2: Another linear transformation (rotation by 90 degrees)
    theta = np.pi / 2
    B = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    print("\nMatrix B (rotation):\n", B)
    print("Is linear transformation:", is_linear_transformation(B))  # Should print True

# QS.3 - Classify the following system as consistent/inconsistent and dependent/independent:

"""
x + 2y = 3
2x + 4y = 6

"""


