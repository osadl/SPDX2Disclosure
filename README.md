# SPDX2Disclosure
Create more verbose versions of an SPDX disclosure file

## Usage
# ./src/SPDX2Disclosure.py --help
usage: SPDX2Disclosure.py [-h] [-l VERBOSITY] [-v] SPDX

positional arguments:
  SPDX                  file name of an SPDX tag:value input file to process

options:
  -h, --help            show this help message and exit
  -l VERBOSITY, --licensing VERBOSITY
                        add licensing information per file, may be "(n)one"
                        (default), "(r)eferenced", or "(t)ext"
  -v, --verbose         show names and texts the program is using

Create several more verbose versions of the disclosure document from the SPDX
tag:value file
