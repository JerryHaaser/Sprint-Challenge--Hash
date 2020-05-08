def get_indices_of_item_weights(weights, length, limit):

    weights_dict = {}
    # iterate through weights
        # check if index[0] + index[1] = limit
            # if yes return tuple
            # if no, move to next index
    for i in range(len(weights)):
        if weights[i] not in weights_dict:
            weights_dict[weights[i]] = [i]
        else:
            weights_dict[weights[i]] += [i]

    for weight in weights:
        if limit - weight in weights_dict:
            if weight == limit - weight:
                return [weights_dict[weight][1], weights_dict[weight][0]]
            if weight > weights_dict[limit-weight][0]:
                return [weights_dict[limit-weight][0], weights_dict[weight][0]]
            else:
                return [weights_dict[weight][0]. weights_dict[limit-weight][0]]

    return None
