import itertools
import operator


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    return (round(accumulated_sum / count, ndigits=2)
            for accumulated_sum, count
            in zip(itertools.accumulate(sequence),
                   itertools.count(1)
                   )
            )


if __name__ == '__main__':
    print(list(running_mean([1, 2, 3])))
    for i in running_mean([1, 2, 3]):
        print(i)
