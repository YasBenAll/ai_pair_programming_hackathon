"""
Fix issues with this untested naive implementation of a convolution.
Also make the convolution faster with help of chat-gpt.

"""
import numpy as np
import matplotlib.pyplot as plt


sample_rate = 100
n_lags = 10
fill_edge = 0

freq_a = 10 * 2 * np.pi
freq_b = 5 * 2 * np.pi
domain = (0, 20 * np.pi)

n_samples = int(domain[1] * sample_rate)
t_axis = np.linspace(domain[0], domain[1], num=n_samples)
signal_a = np.sin(freq_a * t_axis)
signal_b = np.cos(freq_b * t_axis)


def convolute(signal_a, signal_b, n_lags, n_samples):
    conv = np.zeros(n_lags, signal_a.size)
    for lag in range(n_lags):
        lagged_signal_b = signal_b[lag:]
        for index in range(n_samples):
            if index < lagged_signal_b.size:
                conv[lag, index] = signal_a[index] * lagged_signal_b[index]
            else:
                conv[lag, index] = signal_a[index] * fill_edge

    return conv

# code genereated by chat-gpt
def convolute(signal_a, signal_b, n_lags, n_samples):
    padded_signal_b = np.pad(signal_b, (n_lags-1, 0), mode='constant', constant_values=fill_edge)
    conv = np.zeros((n_lags, n_samples))
    for lag in range(n_lags):
        conv[lag, :] = np.convolve(signal_a, padded_signal_b[lag:lag+n_samples], mode='same')
    return conv

def compute_power(conv, n_lags, n_samples):
    power = np.zeros(n_lags)

    for lag in range(n_lags):
        for index in range(n_samples):
            power[lag] += conv[lag, index] ** 2
        power[lag] /= n_samples
    return power


conv = convolute(signal_a, signal_b, n_lags, n_samples)
power = compute_power(conv, n_lags, n_samples)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(list(range(n_lags)), power)
ax.set_xlabel("lags")
ax.set_ylabel("sum of squares")
fig.savefig("convolution.png")
