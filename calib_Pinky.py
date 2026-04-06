'''
calib file using for shortkeck analysis. changed from matlab version calib.m
05/08/2018
'''
import numpy as np

def calib_sk():
	
	calib = {}
	calib["R_SH"] = 0.0030    #Ohms (at 4K, different chip) #same as SK

	calib["M_FB"] = np.array([-24.99]*16)    #same as SK
	calib["M_FB"][2] = -calib["M_FB"][2]
	
	calib["R_WIRE"] = np.array([113.00]*16)    #ohms include in R_FB and R_BIAS; modified
	
	calib["R_BIAS"] = np.array([467.00]*16)
	
	calib["V_B_MAX"] = np.array([2.500, 2.500, 2.500, 2.500, 
						2.500, 2.500, 2.500, 2.500, 
						2.500, 2.500, 2.500, 2.500, 
						2.500, 2.500, 2.500, 2.500])
	
	calib["R_FB"] = np.array([5000.00]*16)
	
	calib["V_FB_MAX"] =  2*np.array([0.975]*16) #V (I think??)
	
	calib["BITS_BIAS"] = 16   # number of bits in TES bias DAC; do we expect this to be the same as SK?
	calib["BITS_FB"] = 14   # number of bits in FB DAC
	
	# Bias ADC bins => bias current (Amps)
	calib["BIAS_CAL"] = (calib["V_B_MAX"]/(2**calib["BITS_BIAS"]))/(calib["R_BIAS"] + calib["R_WIRE"])
	# SQ1 FB DAC bins => TES current (Amps)
	calib["FB_CAL"] = (calib["V_FB_MAX"]/(2**calib["BITS_FB"]))/(calib["R_FB"]+calib["R_WIRE"])/calib["M_FB"]
	return calib
