def preprocess_lines(lines):
    """
    Preprocess lines by stripping whitespace and converting to lowercase.

    Args:
        lines (list): List of lines to preprocess.

    Returns:
        list: Preprocessed lines.
    """
    return [line.strip().lower() for line in lines]
