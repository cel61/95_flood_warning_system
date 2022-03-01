import numpy as np
import matplotlib


def polyfit(dates, levels, p):
    numbered_dates = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(numbered_dates - numbered_dates[0], levels, p)
    poly = np.poly1d(p_coeff)
    result = (poly, numbered_dates[0])
    return result