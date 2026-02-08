def check_seq_lengths(dataset, use_padding):
    """Returns the maximum sequence length and the length of the sequence with
    tokens.

    :param dataset: List of sequences
    :param use_padding: Padding
    :return: Maximum sequence length and length of sequence with tokens
    """
    max_seq_len = max([len(dataset[i][0]) for i in range(len(dataset))])
    print(f"Max Sequence Length: {max_seq_len}")
    same_length = [len(dataset[i][0]) == max_seq_len for i in range(len(dataset))]
    if not all(same_length):
        print("not all sequences are of the same length")

    if use_padding:
        len_with_tokens = max_seq_len + 3
    else:
        len_with_tokens = max_seq_len + 2

    return max_seq_len, len_with_tokens
