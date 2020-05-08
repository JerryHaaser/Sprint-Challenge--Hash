def has_negatives(a):

    """
    YOUR CODE HERE
    """

    result = []
    number_dict = {}
    
    # iterate through list
    # compare first index to all other numbers
    # if other number == first index * -1 append
    for num in a:
        number_dict[num] = None
    for num in a:
        if num > 0:
            if num * -1 in number_dict:
                result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
