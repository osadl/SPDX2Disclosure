# SPDX2Disclosure

## Purpose
Create more verbose versions of an SPDX disclosure file

## Usage and command line options
```bash
SPDX2Disclosure.py --help
```
```
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
```

## Example software bzip2-1.0.8
### Existing files
* <a href="/example/bzip2-1.0.8-OSS-disclosure.txt">bzip2-1.0.8-OSS-disclosure.txt</a>
* <a href="/example/bzip2-1.0.8-SPDX2TV.spdx">bzip2-1.0.8-SPDX2TV.spdx</a>

### Creating more verbose versions of the disclosure document using the SPDX2Disclosure.py script
```bash
SPDX2Disclosure.py bzip2-1.0.8-SPDX2TV.spdx >bzip2-1.0.8-OSS-disclosure-with-copyright-notices-by-file.txt
```
<a href="/example/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-by-file.txt">bzip2-1.0.8-OSS-disclosure-with-copyright-notices-by-file.txt</a>

```bash
SPDX2Disclosure.py bzip2-1.0.8-SPDX2TV.spdx -lr >bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt
```
<a href="/example/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt">bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt</a>

```bash
SPDX2Disclosure.py bzip2-1.0.8-SPDX2TV.spdx -lt >bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt
```
<a href="/example/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt">bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt</a>
