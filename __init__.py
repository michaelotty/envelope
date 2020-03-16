from scipy.signal import hilbert
import numpy as np


def envelope(input_signal):
    baseline_shift = np.mean(input_signal)
    input_signal -= baseline_shift

    analytic_signal = hilbert(input_signal)
    yupper = np.abs(analytic_signal)
    ylower = -np.abs(analytic_signal)

    return (yupper, ylower)

