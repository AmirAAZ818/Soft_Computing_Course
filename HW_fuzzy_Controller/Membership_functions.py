import numpy


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
    assert start < peak < end, "Support is not valid"

    def trimf(x):
        if x <= start or x >= end:
            return 0

        if x == peak:
            return 1

        before_peak_slope = 1 / (peak - start)
        after_peak_slope = 1 / (end - peak)

        if x < peak:
            before_bias = -(start - domain[0]) * before_peak_slope
            res = (before_peak_slope * x) + before_bias

            return res

        if x > peak:
            after_bias = -(end - domain[0]) * after_peak_slope
            res = (after_peak_slope * x) + after_bias

            return res

    return trimf
