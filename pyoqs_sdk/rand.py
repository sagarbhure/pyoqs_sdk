#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
#---------------------------------------------------------------------
# Created By  : Sagar BHURE
# Created Date: 21/11/2021
# version ='1.0'
# --------------------------------------------------------------------


"""
Open Quantum Safe (OQS) Python Wrapper for libpyoqs_sdk

The libpyoqs_sdk project provides post-quantum public key cryptography algorithms:
https://github.com/sagarbhure/libpyoqs_sdk

This module provides a Python 3 interface to libOQS <pyoqs_sdk/rand.h> RNGs.
"""

import pyoqs_sdk


def randombytes(bytes_to_read):
    """
    Generates random bytes. This implementation uses either the default RNG algorithm ("system"), or whichever
    algorithm has been selected by random_bytes_switch_algorithm().

    :param bytes_to_read: the number of random bytes to generate.
    :return: random bytes.
    """
    result = pyoqs_sdk.ct.create_string_buffer(bytes_to_read)
    pyoqs_sdk.native().OQS_randombytes(result, pyoqs_sdk.ct.c_int(bytes_to_read))
    return bytes(result)


def randombytes_switch_algorithm(alg_name):
    """
    Switches the core OQS_randombytes to use the specified algorithm. See <pyoqs_sdk/rand.h> libpyoqs_sdk headers for more details.

    :param alg_name: algorithm name, possible values are "system", "NIST-KAT", "OpenSSL".
    """
    if pyoqs_sdk.native().OQS_randombytes_switch_algorithm(
            pyoqs_sdk.ct.create_string_buffer(alg_name.encode())) != pyoqs_sdk.OQS_SUCCESS:
        raise RuntimeError('Can not switch algorithm')


def randombytes_nist_kat_init_256bit(entropy_input, personalization_string=None):
    """
    Initializes the NIST DRBG with the an entropy seed. The security parameter is 256 bits.

    :param entropy_input: entropy input seed, must be exactly 48 bytes long.
    :param personalization_string: optional personalization string, which, if present, must be at least 48 bytes long.
    """
    if len(entropy_input) != 48:
        raise ValueError('The entropy source must be exactly 48 bytes long')

    if personalization_string is not None:
        if len(personalization_string) < 48:
            raise ValueError('The personalization string must be either empty or at least 48 bytes long')
        pyoqs_sdk.native().OQS_randombytes_nist_kat_init_256bit(pyoqs_sdk.ct.create_string_buffer(entropy_input),
                                                   pyoqs_sdk.ct.create_string_buffer(personalization_string))

    pyoqs_sdk.native().OQS_randombytes_nist_kat_init_256bit(pyoqs_sdk.ct.create_string_buffer(entropy_input), 0)
