import numpy as np
def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the list into a 3x3 NumPy array
    matrix = np.array(input_list).reshape(3, 3)
    
    # Calculate statistics
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Mean of each column
            matrix.mean(axis=1).tolist(),  # Mean of each row
            matrix.mean().tolist()         # Mean of the flattened matrix
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # Variance of each column
            matrix.var(axis=1).tolist(),   # Variance of each row
            matrix.var().tolist()          # Variance of the flattened matrix
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # Standard deviation of each column
            matrix.std(axis=1).tolist(),   # Standard deviation of each row
            matrix.std().tolist()          # Standard deviation of the flattened matrix
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # Max of each column
            matrix.max(axis=1).tolist(),   # Max of each row
            matrix.max().tolist()          # Max of the flattened matrix
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # Min of each column
            matrix.min(axis=1).tolist(),   # Min of each row
            matrix.min().tolist()          # Min of the flattened matrix
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # Sum of each column
            matrix.sum(axis=1).tolist(),   # Sum of each row
            matrix.sum().tolist()          # Sum of the flattened matrix
        ]
    }
    
    return calculations

if __name__ == "__main__":
    input_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]  # This list also has exactly nine elements
    try:
        result = calculate(input_list)
        print(result)
    except ValueError as e:
        print(e)
