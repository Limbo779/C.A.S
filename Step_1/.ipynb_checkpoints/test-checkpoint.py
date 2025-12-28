import librosa as lb
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Set backend explicitly
import matplotlib.pyplot as plt

file = "If_I_Die_Young.flac"

# Load the file
# Note: librosa.load resamples to 22050Hz by default. 
# Use sr=None to keep the file's original sampling rate.
wave, sr = lb.load(file, sr=None) 

# Create time axis in seconds (Vectorized operation, efficient)
# We only need the first 100 points for your plot, so we can just slice wave
# But if you want to plot against time:
times = np.arange(len(wave)) / sr

# Plotting
plt.figure(figsize=(10, 4))
# Plot first 100 samples against their time in seconds
plt.plot(times, wave) 
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Waveform (First 100 Samples)")
plt.show()
