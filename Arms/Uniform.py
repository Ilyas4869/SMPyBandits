# -*- coding: utf-8 -*-
""" Uniformly distributed arm in [0, 1], or [lower, lower + amplitude]."""

__author__ = "Lilian Besson"
__version__ = "0.1"

from numpy.random import random

from .Arm import Arm


class Uniform(Arm):
    """ Uniformly distributed arm in [0, 1], or [lower, lower + amplitude]."""

    def __init__(self, lower=0., amplitude=1.):
        self.lower = lower
        self.amplitude = amplitude

    # --- Random samples

    def draw(self, t=None):
        """ The parameter t is ignored in this Arm."""
        return self.lower + (random() * self.amplitude)

    def draw_nparray(self, shape=(1,)):
        """ The parameter t is ignored in this Arm."""
        return self.lower + (random(shape) * self.amplitude)

    def mean(self):
        return self.lower + (0.5 * self.amplitude)

    # --- Printing

    # This decorator @property makes this method an attribute, cf. https://docs.python.org/2/library/functions.html#property
    @property
    def lower_amplitude(self):
        return (self.lower, self.amplitude)

    def __str__(self):
        return "Uniform"

    def __repr__(self):
        return "U({:.3g}, {:.3g})".format(self.lower, self.amplitude)

    # --- Lower bound

    @staticmethod
    def kl(x, y):
        """ Always 0, as Uniform arms are ALL the same."""
        return 0

    @staticmethod
    def oneLR(mumax, mu):
        """ One term of the Lai & Robbins lower bound for Uniform arms: 0, as Uniform arms are ALL the same."""
        return 0
