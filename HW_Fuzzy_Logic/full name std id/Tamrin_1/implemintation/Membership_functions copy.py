
def trimf_maker(domain, start, peak, end):
    """
    this function returns a method that is a trimf on the domain of X.
    :param domain: domain of the variable we want to fuzzify (a 1d array of len 2)
    :param start: the starting point of mf
    :param peak:  the point in the mf graph where mf(p) = 1
    :param end: the ending point of mf
    :return: a method for trimf in the given domain
    """

    # we should assert this so that the method would be logically valid
    assert start <= peak <= end, "Support is not valid"

    def trimf(x):
        assert domain[0] <= x <= domain[1], "x is not in domain range!"
        if x <= start or x >= end:
            return 0

        if x == peak:
            return 1

        before_peak_slope = 1 / (peak - start) if peak != start else 0
        after_peak_slope = 1 / (peak - end) if peak != end else 0

        if x < peak:
            before_bias = -start * before_peak_slope
            res = (before_peak_slope * x) + before_bias

            return res

        if x > peak:
            after_bias = -end * after_peak_slope
            res = (after_peak_slope * x) + after_bias

            return res

    return trimf


def trapmf_maker(domain, start, peak, end):
    """
    :param domain: 1d array of len 2
    :param start: the starting point
    :param peak:  1d array of len 2, showing the len of the peak value
    :param end: the ending point
    :return: a method that gives you membership capacity for a given x
    """
    assert domain[0] <= start and domain[1] >= end, "Domain or start or end is not valid"
    assert start <= peak[0] <= peak[1] <= end, "parameters are not valid"

    def trapmf(x):

        if peak[0] <= x <= peak[1]:
            return 1

        if x <= start or x >= end:
            return 0

        before_peak_slope = 1 / (peak[0] - start) if peak[0] != start else 0
        after_peak_slope = 1 / (peak[1] - end) if peak[1] != end else 0

        if x < peak[0]:
            before_bias = -start * before_peak_slope
            res = (before_peak_slope * x) + before_bias

            return res

        if x > peak[1]:
            after_bias = -end * after_peak_slope
            res = (after_peak_slope * x) + after_bias

            return res

    return trapmf
