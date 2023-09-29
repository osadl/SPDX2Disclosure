# SPDX2Disclosure

## Purpose
Create more comprehensive versions of an SPDX disclosure file

## Usage and command line options
```bash
SPDX2Disclosure.py --help
```
```
usage: SPDX2Disclosure.py [-h] [-l AMOUNT] [-v] SPDX

positional arguments:
  SPDX                  file name of an SPDX tag:value input file to process

options:
  -h, --help            show this help message and exit
  -l AMOUNT, --licensing AMOUNT
                        licensing information per file to add, may be "(n)one" (default), "(r)eferenced", "(b)sdtext", "(h)ashedtext", or "(t)ext"
  -v, --verbose         show names and texts the program is using

Create several more comprehensive versions of the disclosure document from the SPDX tag:value file
```
## Options

|    Long option      | Short option |                        Function                     |
|:--------------------|:------------:|:----------------------------------------------------|
|licensing=none       |     -ln      | Additional section with copyright notices per file  |
|licensing=referenced |     -lr      | Same as -ln plus all licenses referenced            |
|licensing=bsdtext    |     -lb      | Same as -ln plus non-standard BSD licenses verbatim |
|licensing=hashedtext |     -lh      | Same as -ln plus all hashed licenses verbatim       |
|licensing=text       |     -lt      | Same as -ln plus all licenses verbatim              |

## Program description per command line option
### 1. licensing=none
In a first step, the complete first part of the original OSS Disclosure document will be sent to the program output. Thereafter, new sections for every file of the original package will be appended to the output stream and the

* copyright notices of the package file

will be included in every section.
### 2. licensing=referenced
The original OSS Disclosure document is not used. Instead, new sections for every file of the original package will be sent to the program output, and the

* copyright notices of the package file and
* a reference to the license

will be included in every section. A list of all licenses with references will then be added to the output stream.
### 3. licensing=bsdtext
In a first step, the complete first part of the original OSS Disclosure document will be sent to the program output. Thereafter, new sections for every file of the original package will be appended to the output stream and the

* copyright notices of the package file and,
* if distributed under a non-standard BSD license, the original license text

will be included in every section.
### 4. licensing=hashedtext
In a first step, the complete first part of the original OSS Disclosure document will be sent to the program output. Thereafter, new sections for every file of the original package will be appended to the output stream and the

* copyright notices of the package file and,
* if distributed under any non-standard license as indicated by a hash suffix of the license reference, the original license text

will be included in every section.
### 5. licensing=text
The original OSS Disclosure document is not used. Instead, new sections for every file of the original package will be sent to the program output, and the

* copyright notices of the package file and
* the verbatim text of the licenses

will be included in every section.

## Example no. 1: Program runs on software package <i>bzip2-1.0.8</i>
### Existing files
The following files that are used to exemplify the function of the <i>SPDX2Disclosure.py</i> script are taken from the <a href="https://github.com/Open-Source-Compliance/package-analysis/tree/main/analysed-packages/bzip2/version-1.0.8">related curation data of the OSSelot project</a>.

* SPDX tag:value file: <a href="/example1/bzip2-1.0.8-SPDX2TV.spdx">bzip2-1.0.8-SPDX2TV.spdx</a>
* Default OSS disclosure document: <a href="/example1/bzip2-1.0.8-OSS-disclosure.txt">bzip2-1.0.8-OSS-disclosure.txt</a>

### Command line and resulting more comprehensive version of the disclosure document
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

*  Copyright notices, non-standard BSD-style licenses verbatim and other licenses referenced by file (command line option "-lb")
```bash
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lb >example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt
```
Program output: <a href="/example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt">bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt</a>

*  Copyright notices, all hashed licenses verbatim and other licenses referenced by file (command line option "-lh")
```bash
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lh >example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-hashed-licenses-verbatim-and-other-licenses-referenced-by-file.txt
```
Program output: <a href="/example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-hashed-licenses-verbatim-and-other-licenses-referenced-by-file.txt">bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt</a>

* Copyright notices and verbatim licenses by file (command line option "-lt")
```bash
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lt >example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt
```
Program output: <a href="/example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt">bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt</a>

## Example no. 2: Program runs on software package <i>init-system-helpers-debian-1.65.2</i>
### Existing files
The following files that are used to exemplify the function of the <i>SPDX2Disclosure.py</i> script are taken from the <a href="https://github.com/Open-Source-Compliance/package-analysis/tree/main/analysed-packages/init-system-helpers-debian/version-1.65.2">related curation data of the OSSelot project</a>.

* SPDX tag:value file: <a href="/example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx">init-system-helpers-debian-1.65.2-SPDX2TV.spdx</a>
* Default OSS disclosure document: <a href="/example2/init-system-helpers-debian-1.65.2-OSS-disclosure.txt">init-system-helpers-debian-1.65.2-OSS-disclosure.txt</a>

### Command line and resulting more comprehensive version of the disclosure document
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

*  Copyright notices, all hashed licenses verbatim and other licenses referenced by file (command line option "-lh")
```bash
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -lh >example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-hashed-licenses-verbatim-and-other-licenses-referenced-by-file.txt
```
Program output: <a href="/example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-hashed-licenses-verbatim-and-other-licenses-referenced-by-file.txt">init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt</a>

* Copyright notices and verbatim licenses by file (command line option "-lt")
```bash
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -lt >example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt
```
Program output: <a href="/example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt">init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt</a>

## Example no. 3: Program runs on software package <i>busybox-1.36.1</i>
### Existing files
The following files that are used to exemplify the function of the <i>SPDX2Disclosure.py</i> script are taken from the <a href="https://github.com/Open-Source-Compliance/package-analysis/tree/main/analysed-packages/init-system-helpers-debian/version-1.65.2">related curation data of the OSSelot project</a>.

* SPDX tag:value file: <a href="/example3/busybox-1.36.1-SPDX2TV.spdx">busybox-1.36.1-SPDX2TV.spdx</a>
* Default OSS disclosure document: <a href="/example3/busybox-1.36.1-OSS-disclosure.txt">busybox-1.36.1-OSS-disclosure.txt</a>

### Command line and resulting more comprehensive version of the disclosure document
* Copyright notices by file (no command line option)
```bash
./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx >example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-by-file.txt
```
Program output: <a href="/example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-by-file.txt">busybox-1.36.1-OSS-disclosure-with-copyright-notices-by-file.txt</a>

*  Copyright notices and referenced licenses by file (command line option "-lr")
```bash
./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx -lr >example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt
```
Program output: <a href="/example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt">busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt</a>

*  Copyright notices, BSD-style licenses verbatim and other licenses referenced by file (command line option "-lb")
```bash
./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx -lb >example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt
```
Program output: <a href="/example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt">busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt</a>

*  Copyright notices, all hashed licenses verbatim and other licenses referenced by file (command line option "-lh")
```bash
./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx -lh >example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-hashed-licenses-verbatim-and-other-licenses-referenced-by-file.txt
```
Program output: <a href="/example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-hashed-licenses-verbatim-and-other-licenses-referenced-by-file.txt">busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt</a>

* Copyright notices and verbatim licenses by file (command line option "-lt")
```bash
./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx -lt >example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt
```
Program output: <a href="/example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt">busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt</a>
