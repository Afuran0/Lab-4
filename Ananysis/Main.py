import pandas as pd

# Load the dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Selection Sort
def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j]['Date'] < data[min_index]['Date']:
                min_index = j
        # Make the minimum element appear as the first element 
        data[i], data[min_index] = data[min_index], data[i]
    return data

# Insertion Sort 
def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and key['Date'] < data[j]['Date']:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key  
    return data  

# Main function for sorting 
def main(file_path):
    df = load_data(file_path)
    print("Original Dataset:")
    print(df.head())
    
    
    data_list = df.to_dict(orient='records')
    
    # Selection sort
    sorted_selection = selection_sort(data_list.copy())
    print("\nSorted Dataset using Selection Sort:")
    print(pd.DataFrame(sorted_selection).head())
    
    # Insertion sort 
    sorted_insertion = insertion_sort(data_list.copy())
    print("\nSorted Dataset using Insertion Sort:")
    print(pd.DataFrame(sorted_insertion).head())

# Example usage
file_path = 'budget_data.csv'  
main(file_path)

