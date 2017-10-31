#!/usr/bin/python

import math
import random

from orbit import Orbit
from pulsar import Pulsar
import galacticops as go

# Binary system for Neutron Star - Neutron star configuration

class NsNsException(Exception):
    pass

class NSNS(Orbit):
    '''
    Class to store two NS objects
    '''
    def __init__(self,po,pmass,cmass,peri,inc,ecc):
        '''
        Pulsar1 should always be MSP or lesser period pulsar
        and Pulsar2 should be companion
        '''
        self.pulsar1 = Pulsar()
        self.pulsar2 = Pulsar()

        super(NSNS,self).__init__(is_binary=True,
        type='NS-NS',
        orbital_period_days=po,
        pulsar_mass_msolar=pmass,
        companion_mass_msolar=cmass,
        long_peri_degrees=peri,
        inclination_degrees=inc,
        eccentricity=ecc)

        # center of mass coordinates which evolve
        self.gl_cm = None
        self.gb_cm = None
