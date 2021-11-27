#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
#---------------------------------------------------------------------
# Created By  : Sagar BHURE
# Created Date: 21/11/2021
# version ='1.0'
# --------------------------------------------------------------------

# key encapsulation Python example

from pprint import pprint
import f5oqs_sdk

######################################################################
# KEM example
######################################################################

kems = f5oqs_sdk.get_enabled_KEM_mechanisms()

print("Enabled KEM mechanisms:")
pprint(kems, compact="True")

# create client and server with sample KEM mechanisms
kemalg = str(input(' Enter key encapsulation mrchanism: ')) #"Kyber512"
with f5oqs_sdk.KeyEncapsulation(kemalg) as client:
    with f5oqs_sdk.KeyEncapsulation(kemalg) as server:
        print("\nKey encapsulation details:")
        pprint(client.details)

        # client generates its keypair
        public_key = client.generate_keypair()
        # optionally, the secret key can be obtained by calling export_secret_key()
        # and the client can later be re-instantiated with the key pair:
        # secret_key = client.export_secret_key()
        # store key pair, wait... (session resumption):
        # client = f5oqs_sdk.KeyEncapsulation(kemalg, secret_key)

        # the server encapsulates its secret using the client's public key
        ciphertext, shared_secret_server = server.encap_secret(public_key)

        # the client decapsulates the the server's ciphertext to obtain the shared secret
        shared_secret_client = client.decap_secret(ciphertext)
        pprint( ciphertext)
        print("\nShared secretes coincide:", shared_secret_client == shared_secret_server)
