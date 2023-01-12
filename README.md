
# Quantum-Proof Security with f5oqs_sdk in Python 

[![Build status](https://www.python.org/static/community_logos/python-logo.png)](https://pypi.org/project/f5oqs-sdk/)

[![Build status](https://ci.appveyor.com/api/projects/status/jjo1ti9l5e0grgln?svg=true)](https://github.com/sagarbhure/f5oqs_sdk/releases/tag/v2.0) ![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)  ![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)  ![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)  ![License](https://img.shields.io/badge/license-MIT-blue.svg)

f5oqs_sdk PyPi : https://pypi.org/project/f5oqs-sdk/

The Open Quantum Safe (OQS) project has the goal of developing and prototyping quantum-resistant cryptography.
liboqs is an open source C library for quantum-resistant cryptographic algorithms. See more about liboqs at https://github.com/open-quantum-safe/liboqs/, including a list of supported algorithms.



f5oqs_sdk is an open-source Python 3 library that wraps the liboqs C library. It offers a unified API for post-quantum key encapsulation and digital signature schemes, as well as a collection of open-source implementations of post-quantum cryptography algorithms. 

The OQS project also includes prototype integrations into various application-level protocols to test the effectiveness of quantum-resistant cryptography. For more information, visit https://openquantumsafe.org/
## Pre-requisite
Python 3.x f5oqs_sdk depends on the liboqs C library; liboqs must first be compiled as a Linux/macOS/Windows library.
## Contents 

This Project contains following Contents

- `f5oqs_sdk/f5oqs_sdk.py`: a Python 3 module wrapper for the liboqs C library.
- `f5oqs_sdk/rand.py`: a Python 3 module supporting RNGs from <oqs/rand.h>
- `test`: unit test to be added



## Installation

This project is on [PyPI](https://pypi.org/project/f5oqs-sdk/) and can be installed with

```
pip install f5oqs_sdk
```


First, you must build liboqs according to the liboqs building instructions with shared library support enabled (add `-DBUILD_SHARED_LIBS=ON` to the cmake command), followed (optionally) by a sudo ninja install to ensure that the shared library is visible system-wide (by default it installs under `/usr/local/include` and `/usr/local/lib` on Linux/macOS).

On Linux/macOS you may need to set the `LD_LIBRARY_PATH` (`DYLD_LIBRARY_PATH` on macOS) environment variable to point to the path to liboqs' library directory, e.g.
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
```

Alternatively, you can install it from this repository directly:

```
git clone https://github.com/sagarbhure/f5oqs_sdk
cd f5oqs_sdk
python3 setup.py install
```


## Running Tests [In-progress]



To run the unit tests without a test runner:
```
python3 tests/test_kem.py
python3 tests/test_sig.py
```

## Usage

The f5oqs_sdk library offers two main classes, KeyEncapsulation and Signature, for implementing post-quantum key encapsulation and signature mechanisms. To use these classes, you must instantiate them with a string that identifies one of the mechanisms supported by liboqs.

You can use the get_enabled_KEM_mechanisms() and get_enabled_sig_mechanisms() functions to enumerate the available options. The examples in the examples/ directory show how to use the library's API. Additionally, the library supports alternative RNGs through the randombytes[] functions.
## Authors

- [@sagarbhure](https://www.github.com/sagarbhure)

