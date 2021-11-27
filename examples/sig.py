#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
#---------------------------------------------------------------------
# Created By  : Sagar BHURE
# Created Date: 21/11/2021
# version ='1.0'
# --------------------------------------------------------------------

# signature Python example

from pprint import pprint
import f5oqs_sdk

######################################################################
# signature example
######################################################################

sigs = f5oqs_sdk.get_enabled_sig_mechanisms()

print("Enabled signature mechanisms:")
pprint(sigs, compact="True")

message = "This is the message to sign".encode()
pprint(message)

# create signer and verifier with sample signature mechanisms
sigalg = str(input('Enter signature mechanism: '))  #"Dilithium2"
with f5oqs_sdk.Signature(sigalg) as signer:
    with f5oqs_sdk.Signature(sigalg) as verifier:
        print("\nSignature details:")
        pprint(signer.details)

        # signer generates its keypair
        signer_public_key = signer.generate_keypair()

        # signer signs the message
        signature = signer.sign(message)

        # verifier verifies the signature
        is_valid = verifier.verify(message, signature, signer_public_key)

        print("\nValid signature?", is_valid)
