import numpy as np


def rfft(data):
    # Compute real fft of data
    return np.fft.rfft(data)


def fft(data):
    # Compute fft of data
    return np.fft.fft(data)


def compute_auto_correlation(data):
    # Compute auto correlation function of data
    # for the autocorrelation function, we want the overlap between
    # the first vector at time 0 and all
    # subsequent vectors at later times
    # - the sum of the product of initial and
    # subsequent vectors for each time step
    auto_corr = np.zeros(data.shape[0], dtype="complex")
    for i in range(data.shape[0]):
        auto_corr[i] = np.vdot(data[0, :], data[i, :])
    return data


def compute_auto_corr_dft(data):
    # Compute dft of auto correlation function of data
    return fft(compute_auto_correlation(data))
