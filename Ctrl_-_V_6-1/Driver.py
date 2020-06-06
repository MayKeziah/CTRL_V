import AudioInput as AI
import numpy as np
import Sampler
import Signatures
import json

# # ==========================================================================
# # Load relevant global variables

with open('Global_Variables.json') as var:
	args = json.load(var)

block_duration = args['block_duration']
fftsize = args['n-point']
phi = args['Phi']
phrases = args['phrases']

# # ==========================================================================

# # Generate signatures
# # print("**** Cleaning Brine")
# # Sampler.cleanBrine()
# # print("**** Generating Brine")
# # Sampler.generateBrine()
print("**** Generating Signatures")
Signatures.generateSignatures(True)

# Run real-time test
print("**** Starting Audio Input Stream")
AI.audioInputStream(True)

# # a = np.arange(9)
# # b = np.arange(4,13)

# # c = a.reshape((3,3))
# # d = b.reshape((3,3))

# # print(Sampler.rms(c,d))
# # print(Sampler.rms(a,b))

# # print(c)

# import os
# import pickle

# path = os.getcwd() + '\\Brine\\Signatures.pickle'
# pickle_in = open(path, 'rb')
# sigs = pickle.load(pickle_in)
# pickle_in.close()

# Sampler.printSpectrogram(sigs['Down'])