# create a sample list of numbers
# create a function that takes the sample list and returns a list of even numbers from the sample list
# return the list of even numbers
# Example: [1, 2, 3, 4, 5, 6, 7, 8, 9] -> [2, 4, 6, 8]

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even(sample):
    return [i for i in sample if i % 2 == 0]

print(even(sample_list))