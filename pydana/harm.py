import numpy as np


def rfft(data):
    # Compute real fft of data
    return np.fft.rfft(data)


def fft(data):
    # Compute fft of data
    return np.fft.fft(data)


def compute_auto_correlation(data):
    # Compute auto correlation function of data
    pass


def compute_auto_corr_dft(data):
    # Compute dft of auto correlation function of data
    pass
