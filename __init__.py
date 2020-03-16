from scipy.signal import hilbert
import numpy as np


def envelope(input_signal):
    baseline_shift = np.mean(input_signal)
    normalised_signal = input_signal - baseline_shift

    analytic_signal = hilbert(normalised_signal)
    yupper = np.abs(analytic_signal) + baseline_shift
    ylower = -np.abs(-analytic_signal) + baseline_shift

    return (yupper, ylower)

