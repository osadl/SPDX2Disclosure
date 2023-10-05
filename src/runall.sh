#!/bin/bash

./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx >example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-by-file.txt
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lr -p >example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lt -p >example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lb -p >example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lh -p >example1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-hashed-licenses-verbatim-and-other-licenses-referenced-by-file.txt

./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx >example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-by-file.txt
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -lr -p >example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -lt -p >example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -lb -p >example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -lh -p >example2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-hashed-licenses-verbatim-and-other-licenses-referenced-by-file.txt

./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx >example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-by-file.txt
./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx -lr -p >example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt
./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx -lt -p >example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt
./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx -lb -p >example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt
./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx -lh -p >example3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-hashed-licenses-verbatim-and-other-licenses-referenced-by-file.txt
