#!/usr/bin/python
from orbit import Orbit

class BHNSException(Exception):
    pass


class BHNS(Pulsar):
    """ Class to store an individual pulsar"""
    def __init__(self):
        """___init___ function for the Orbit class"""
