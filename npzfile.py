import numpy as np
from warnings import warn
from scipy import io
import gfd

class Calculations(object):

    def __init__(self, fname):
        """Wrapper for npz files"""
        self.npz = np.load(fname)
        if self.npz['z'].ndim == 2:
            self.Ny, self.Nx = self.npz['z'].shape
        elif self.npz['z'].ndim == 3:
            warn('This module only takes 2D matrices')
            exit()

    def derivative(self, varname='Amp', xname='x', yname='y'):
        """Return the first order derivative field"""
        T = self.npz[varname][:]
        x = self.npz[xname][:]
        y = self.npz[yname][:]

        dTx = .5 * ( (np.roll(T,-1,axis=1) - T) + (T - np.roll(T,1,axis=1)) )
        dTy = .5 * ( (np.roll(T,-1,axis=0) - T) + (T - np.roll(T,1,axis=0)) )

        dx = .5 * ( (np.roll(x,-1) - x) + (x - np.roll(x,1)) )
        dy = .5 * ( (np.roll(y,-1) - y) + (y - np.roll(y,1)) )

        dTx_dx = dTx / dx[np.newaxis, :]
        dTy_dy = dTy / dy[:, np.newaxis]

        return dTx_dx, dTy_dy, x, y

    def gradient_modulus(self, varname='Amp', xname='x', yname='y'):
        """Return the modulus of the gradient of T at the tracer point."""
        T = self.npz[varname][:]
        x = self.npz[xname][:]
        y = self.npz[yname][:]

        dTx = np.roll(T,-1,axis=1) - T
        dTy = np.roll(T,-1,axis=0) - T

        dx = np.roll(x,-1) - x
        dy = np.roll(x,-1) - y

        return np.sqrt( 0.5 *
                    ((dTx**2 + np.roll(dTx,1,axis=0)**2) / dx**2
                   +(dTy**2 + np.roll(dTy,1,axis=1)**2) / dy**2)
        )
