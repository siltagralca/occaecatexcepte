import numpy as np

# Simulated decoder output: a batch of audio features
# Shape (batch_size, time_steps, features)
decoder_outputs = np.random.rand(1, 100, 128)  # Example shape

# Accessing the first element in the batch, first time step, first feature
output_audio = decoder_outputs[0][0, 0]

print("Output audio value:", output_audio)
