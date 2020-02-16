def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    sequence = list(sequence.upper())
    counts = {}
    for base in 'AGCT':
        counts[base] = sequence.count(base)
    gc_content = (counts['C'] + counts['G']) / sum(counts.values()) * 100
    return round(gc_content, ndigits=2)
