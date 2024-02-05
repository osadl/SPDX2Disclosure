#!/bin/bash

for i in example?
do
  rsync -a $i/ new$i/
done

./src/SPDX2Disclosure.py example0/bzip2-1.0.8-SPDX2TV.spdx -cnp >example0/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-by-file.txt
./src/SPDX2Disclosure.py example0/bzip2-1.0.8-SPDX2TV.spdx -lr -cnp >newexample0/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt
./src/SPDX2Disclosure.py example0/bzip2-1.0.8-SPDX2TV.spdx -lr -cnp -w80 >newexample0/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file-maxlen80.txt
./src/SPDX2Disclosure.py example0/bzip2-1.0.8-SPDX2TV.spdx -lt -cnp >newexample0/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt
./src/SPDX2Disclosure.py example0/bzip2-1.0.8-SPDX2TV.spdx -lb -cnp >newexample0/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt
./src/SPDX2Disclosure.py example0/bzip2-1.0.8-SPDX2TV.spdx -lh -cnp >newexample0/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-hashed-licenses-verbatim-and-other-licenses-referenced-by-file.txt

./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -cnp >newexample1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-by-file.txt
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lr -cnp >newexample1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lr -cnp -w80 >newexample1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file-maxlen80.txt
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lt -cnp >newexample1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lb -cnp >newexample1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt
./src/SPDX2Disclosure.py example1/bzip2-1.0.8-SPDX2TV.spdx -lh -cnp >newexample1/bzip2-1.0.8-OSS-disclosure-with-copyright-notices-and-hashed-licenses-verbatim-and-other-licenses-referenced-by-file.txt

./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -cnp >newexample2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-by-file.txt
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -lr -cnp >newexample2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -lr -cnp -w80 >newexample2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file-maxlen80.txt
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -lt -cnp >newexample2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -lb -cnp >newexample2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt
./src/SPDX2Disclosure.py example2/init-system-helpers-debian-1.65.2-SPDX2TV.spdx -lh -cnp >newexample2/init-system-helpers-debian-1.65.2-OSS-disclosure-with-copyright-notices-and-hashed-licenses-verbatim-and-other-licenses-referenced-by-file.txt

./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx -cnp >newexample3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-by-file.txt
./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx -lr -cnp >newexample3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file.txt
./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx -lr -cnp -w80 >newexample3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-referenced-licenses-by-file-maxlen80.txt
./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx -lt -cnp >newexample3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-verbatim-licenses-by-file.txt
./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx -lb -cnp >newexample3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-BSD-licenses-verbatim-and-other-licenses-referenced-by-file.txt
./src/SPDX2Disclosure.py example3/busybox-1.36.1-SPDX2TV.spdx -lh -cnp >newexample3/busybox-1.36.1-OSS-disclosure-with-copyright-notices-and-hashed-licenses-verbatim-and-other-licenses-referenced-by-file.txt

for i in example?
do
  result=`diff -rq $i/ new$i/`
  if test "$result"
  then
    echo Error in $i
    exit 1
  fi
done

rm -Rf newexample?

exit 0
