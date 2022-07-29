# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/28/2022
# Description: Generates a sequence that counts the number of contiguous equal digits and uses the count as a part
#               of the next sequence.


def count_seq():
    """Generates a sequence that counts the number of contiguous equal digits and uses the count as a part of the
    next sequence."""

    term = "2"

    while True:

        new_term = ""

        count = 0

        for i in range(0, len(term)):

            count += 1

            if i+1 >= len(term) or term[i] != term[i+1]:

                new_term += str(count) + term[i]

                count = 0

        print(term)

        term = new_term
