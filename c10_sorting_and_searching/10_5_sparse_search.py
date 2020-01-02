# 10.5 Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
# method to find the location of a given string.
# EXAMPLE
# Input: ball,{"at", "", "", "ball", "", "",# ""}
# Output:4

# Solutions:
# single search -0 binary search with  looking around when middle is an ""
# multiple searches :  group in a dict structure and have o(1) operations

def transform(data):
    transformed_data = {}
    for (index,element) in enumerate(data):
        if element in transformed_data:
            transformed_data[element].append(index)
        else:
            transformed_data[element] = [index]
    print(transformed_data)
    return  transformed_data

data = ["ana", "", "", "ana", "are", "mere"]
data_dict = transform(data)
element = "ana"
print(data_dict.get(element, None))