# 3rd party
from collections import Counter


def get_trick_dict(list):
    # Print the landed tricks and their counter to the skater
    result_landed = Counter(list)

    # Using an anonymous function (lambda function) in order to sort dict by count
    # Descending order
    sorted_result = sorted(result_landed.items(),
                           key=lambda x: x[-1], reverse=True)

    # Hence the sorted function returns a tuple, it has to be converted into a dict again
    converted_dict = dict(sorted_result)

    # Printing each key and value in the dict
    for key, value in converted_dict.items():
        print(f"{key}: {value}")
