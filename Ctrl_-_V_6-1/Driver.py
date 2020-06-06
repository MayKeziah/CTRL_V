import AudioInput as AI
import numpy as np
import Sampler
import Signatures
import json

# ==========================================================================
# Load relevant global variables

with open('Global_Variables.json') as var:
	args = json.load(var)

block_duration = args['block_duration']
fftsize = args['n-point']
phi = args['Phi']
phrases = args['phrases']

# ==========================================================================

# Generate signatures
Sampler.cleanBrine()
Sampler.generateBrine()
Signatures.generateSignatures(True)

# Run real-time test
AI.audioInputStream(True)

# a = np.arange(9)
# b = np.arange(4,13)

# c = a.reshape((3,3))
# d = b.reshape((3,3))

# print(Sampler.rms(c,d))
# print(Sampler.rms(a,b))

# print(c)

