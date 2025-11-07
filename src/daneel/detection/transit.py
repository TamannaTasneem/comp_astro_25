import batman
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib import rc

def transit(args):

    params = batman.TransitParams()
    params.t0 = args['t0']
    params.per = args['per']
    params.rp = args['rp']
    params.a = args['a']
    params.inc = args['inc']
    params.ecc = args['ecc']
    params.w = args['w']
    params.u = [args['u1'], args['u2']]
    params.limb_dark = args['limb_dark']
   
    t = np.linspace(-0.025, 0.025, 1000)  	#times at which to calculate light curve	
    m = batman.TransitModel(params, t)      #initializes model

    flux = m.light_curve(params)		#calculates light curve
    plt.plot(t, flux)


    plt.xlabel("Time from central transit (days)")
    plt.ylabel("Relative flux")
    #plt.ylim((0.975, 1.001))

    plt.savefig("WASP_60_b_assignment1_taskF.png")

    plt.show()