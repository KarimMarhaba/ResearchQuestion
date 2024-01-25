import numpy as np


def complex_conversion(data):
    # This function
    # corrects the data representation: this is in
    # fact a complex matrix the real part of each
    # matrix column is contained in numpy array
    # column 0, 2, 4, 6, ... the imaginary part of
    # each matrix column is contained in numpy array
    # column 1, 3, 5, 7, ... convert the array that
    # was read as dtype=float into a dtype=complex array
    data = np.ndarray.astype(data, dtype="complex")
    data_complex = data[:, 0:-1:2] + 1j * data[:, 1::2]
    return data_complex


def strip_time(arr):
    # Selects first column and all but first column
    time_col = arr[:, 0]
    data = arr[:, 1:]
    return data, time_col
