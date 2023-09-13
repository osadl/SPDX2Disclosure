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
                        add licensing information per file, may be "(n)one" (default), "(r)eferenced", "(b)sdtext", or "(t)ext"
  -v, --verbose         show names and texts the program is using

Create several more verbose versions of the disclosure document from the SPDX tag:value file
```
## Options

|    Long option      | Short option |                        Function                    |
|:--------------------|:------------:|:---------------------------------------------------|
|licensing=none       |     -ln      | Additional section with copyright notices per file |
|licensing=referenced |     -lr      | Same as -ln plus referenced licenses               |
|licensing=bsdtext    |     -lb      | Same as -ln plus verbatim BSD licenses             |
|licensing=text       |     -lt      | Same as -ln plus all licenses verbatim             |

## Example no. 1: Program runs on software package <i>bzip2-1.0.8</i>
### Existing files
The following files that are used to exemplify the function of the <i>SPDX2Disclosure.py</i> script are taken from the <a href="https://github.com/Open-Source-Compliance/package-analysis/tree/main/analysed-packages/bzip2/version-1.0.8">related curation data of the OSSelot project</a>.
* SPDX tag:value file: <a href="/example1/bzip2-1.0.8-SPDX2TV.spdx">bzip2-1.0.8-SPDX2TV.spdx</a>
* Default OSS disclosure document: <a href="/example1/bzip2-1.0.8-OSS-disclosure.txt">bzip2-1.0.8-OSS-disclosure.txt</a>

### Command line and resulting more verbose version of the disclosure document
* Copyright notices by file (no command line option)
```bash
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx >example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-by-file.txt
```
Program output: <a href="/example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-by-file.txt">bzip2-1.0.8-OSS-disclosure-with-copyright-notices-by-file.txt</a>

*  Copyright notices and referenced licenses by file (command line option "-lr")
```bash
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lr >example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt
```
Program output: <a href="/example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt">bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt</a>

*  Copyright notices, BSD-style licenses verbatim and other licenses referenced by file (command line option "-lb")
```bash
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lb >example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt
```
Program output: <a href="/example1/bzip2-1.0.8-1.65.2-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt">bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt</a>

* Copyright notices and verbatim licenses by file (command line option "-lt")
```bash
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lt >example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt
```
Program output: <a href="/example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt">bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt</a>

## Example no. 2: Program runs on software package <i>init-system-helpers-debian-1.65.2</i>
### Existing files
The following files that are used to exemplify the function of the <i>SPDX2Disclosure.py</i> script are taken from the <a href="https://github.com/Open-Source-Compliance/package-analysis/tree/main/analysed-packages/bzip2/version-1.0.8">related curation data of the OSSelot project</a>.
* SPDX tag:value file: <a href="/example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx">init-system-helpers-debian-1.65.2-SPDX2TV.spdx</a>
* Default OSS disclosure document: <a href="/example2/init-system-helpers-debian-1.65.2-OSS-disclosure.txt">init-system-helpers-debian-1.65.2-OSS-disclosure.txt</a>

* Copyright notices by file (no command line option)
```bash
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx >example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-by-file.txt
```
Program output: <a href="/example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-by-file.txt">init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-by-file.txt</a>

*  Copyright notices and referenced licenses by file (command line option "-lr")
```bash
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -lr >example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt
```
Program output: <a href="/example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt">init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt</a>

*  Copyright notices, BSD-style licenses verbatim and other licenses referenced by file (command line option "-lb")
```bash
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -lb >example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt
```
Program output: <a href="/example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt">init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt</a>

* Copyright notices and verbatim licenses by file (command line option "-lt")
```bash
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -lt >example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt
```
Program output: <a href="/example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt">init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt</a>
