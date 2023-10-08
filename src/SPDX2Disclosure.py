#!/usr/bin/env python3

# This software is licensed under GPL-3.0
# Copyright (c) 2023 Open Source Automation Development Lab (OSADL) eG <info@osadl.org>
# Author Carsten Emde <C.Emde@osadl.org>

import argparse
import textwrap
import re

def ishex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def hashexsuffix(licensename):
    parts = licensename.split('-')
    suffix = parts[len(parts) - 1]
    return ishex(suffix)

def wrapprint(text, maxlen):
    if maxlen == 0:
        print(text)
    else:
        text = re.sub('([^\n])\n([^\n])', '\\1 \\2', text)
        lines = text.split('\n')
        wrapper = textwrap.TextWrapper(width=maxlen, replace_whitespace=False)
        newtext = ''
        for line in lines:
            newtext += wrapper.fill(line) + '\n'
        print(newtext.rstrip())

def getlicenselist(filename):
    filename = filename.replace('-SPDX2TV.spdx', '-OSS-disclosure.txt')
    f = open(filename, 'r')
    licenselist = ''
    for line in f:
        licenselist += line
        if line.startswith('Copyright notices'):
            break;
    f.close()
    return licenselist.strip()

def collectlicenses(filename, showpreamble):
    licenses = {}
    preamble = {}
    f = open(filename, 'r')
    intext = False
    preambletags = ['PackageName', 'PackageVerificationCode', 'PackageChecksum', 'PackageLicenseConcluded']

    for line in f:
        if showpreamble and len(preamble) < 4:
            for p in preambletags:
                if line.startswith(p + ': '):
                    preamble[p] = line[len(p) + 2:].rstrip()
        if not intext:
            if line.startswith('LicenseID: '):
                ref = line[11:].rstrip()
                continue
            if line.startswith('ExtractedText: '):
                licensetext = ''
                intext = True
        if intext:
            cleanline = line.replace('ExtractedText: ', '')
            cleanline = cleanline.replace('<text>', '').replace('</text>', '').strip()
            licensetext += cleanline + '\n'
            if line.find('</text>') != -1:
                intext = False
                licenses[ref] = licensetext.strip()
    f.close()
    return preamble, licenses

def SPDX2Disclosure(filename, licenselevel, showchecksums, shownumbers, showpreamble, verbose, maxlen):
    preamble, licenses = collectlicenses(filename, showpreamble)
    if showpreamble:
        for key, val in preamble.items():
            print(key, ': ', val, sep='')
        print('-'*8,'\n', sep='')

    if licenselevel in [0, 2, 3]:
        alllicenses = getlicenselist(filename)
        alllicenses = alllicenses.replace('LICENSES \n', 'LICENSES\n(See the details below for the assignment of licenses to files.)\n', 1)
        if licenselevel == 0: 
            print(alllicenses, 'by file:\n')
        else:
            print(alllicenses, 'and licenses by file:\n')

    f = open(filename, 'r')
    first = True
    infile = False
    incopyright = False
    licensesinuse = []
    n = 1
    for line in f:
        line = line.rstrip()
        if line.startswith('LicenseID: '):
            break
        if line.startswith('FileName: '):
            if verbose:
                print('Found entry of file ', line[10:].rstrip())
            copyrightnotice = ''
            sha1 = ''
            sha256 = ''
            md5 = ''
            file = line[10:].rstrip()
            infile = True
            continue
        if infile:
            if showchecksums:
                if line.startswith('FileChecksum: SHA1: '):
                    sha1 = line[20:].strip()
                if line.startswith('FileChecksum: SHA256: '):
                    sha256 = line[22:].strip()
                if line.startswith('FileChecksum: MD5: '):
                    md5 = line[19:].strip()
            if line.startswith('LicenseConcluded: '):
                licensenotices = line[18:].strip().replace(' OR ', ' AND ').split(' AND ')
            if line.startswith('FileCopyrightText: '):
                incopyright = True
            if incopyright:
                cleanline = line.replace('FileCopyrightText: ', '')
                cleanline = cleanline.replace('<text>', '').replace('</text>', '').strip()
                if len(cleanline) > 0:
                    if len(copyrightnotice) == 0:
                        copyrightnotice = cleanline
                    else:
                        copyrightnotice += '\n' + cleanline
                if line.find('</text>') != -1 or cleanline == 'NOASSERTION':
                    infile = False
                    incopyright = False
                    needsection = False
                    haslicense = False
                    if licenselevel > 0:
                        if licensenotices[0] != 'NOASSERTION':
                            haslicense = True
                    if copyrightnotice != 'NOASSERTION' or haslicense:
                        if first:
                            first = False
                        else:
                            print('-'*8)
                        if shownumbers:
                            print('FileName(' + str(n) + '): ' + file + ':')
                            n = n + 1
                        else:
                            print('FileName: ' + file + ':')
                        if showchecksums:
                            if sha1 != '':
                                print('FileChecksum: SHA1:', sha1)
                            if sha256 != '':
                                print('FileChecksum: SHA256:', sha256)
                            if md5 != '':
                                print('FileChecksum: MD5:', md5)
                        needsection = True
                    else:
                        if verbose:
                            print('Warning: Skipped file ' + file)
                            print()
                    if copyrightnotice != 'NOASSERTION':
                        if licenselevel > 0:
                            print('FileCopyrightText:')
                        wrapprint(copyrightnotice, maxlen)
                    if licenselevel > 0 and haslicense:
                        if len(copyrightnotice) > 0 and copyrightnotice != 'NOASSERTION':
                            print()
                        print('LicenseConcluded:')
                        for licensename in licensenotices:
                            if licensename != 'NOASSERTION':
                                if licensename not in licensesinuse:
                                    licensesinuse.append(licensename)
                                if (licenselevel == 2 and 'BSD' in licensename and hashexsuffix(licensename)) or\
                                  (licenselevel == 3 and hashexsuffix(licensename)) or licenselevel == 4:
                                    print(licensename + ':')
                                    wrapprint(licenses[licensename], maxlen)
                                    print()
                                else:
                                    print(licensename)
                                needsection = True
                    copyrightnotice = ''
                    if needsection:
                        print()
    if licenselevel == 1:
        print('-'*8,'\n', sep='')
        print('\nReferenced licenses:')
        print('-'*20,'\n', sep='')
        first = True
        for k in licenses:
            if k in licensesinuse:
                if first:
                    first = False
                else:
                    print('\n','-'*8, sep='')
                print(k + ':')
                wrapprint(licenses[k], maxlen)
    f.close

def main():
    errorhelp = 'may be "(n)one" (default), "(r)eferenced", "(b)sdtext", "(h)ashedtext", or "(t)ext"'
    parser = argparse.ArgumentParser(prog = 'SPDX2Disclosure.py',
        epilog = 'Create several more comprehensive versions of the disclosure document from the SPDX tag:value file')

    parser.add_argument('filename',
      metavar = 'SPDX',
      help = 'file name of an SPDX tag:value input file to process')
    parser.add_argument('-l', '--licensing',
      metavar = 'AMOUNT',
      default = 'none',
      help = 'licensing information per file to add, ' + errorhelp)
    parser.add_argument('-c', '--checksums',
      action = 'store_true',
      default = False,
      help = 'include SHA1, SHA256 and MD5 checksums')
    parser.add_argument('-n', '--numbered',
      action = 'store_true',
      default = False,
      help = 'files are consecutively numbered')
    parser.add_argument('-p', '--preamble',
      action = 'store_true',
      default = False,
      help = 'prepend general package data')
    parser.add_argument('-v', '--verbose',
      action = 'store_true',
      default = False,
      help = 'show names and texts the program is using')
    parser.add_argument('-w', '--width',
      metavar = 'N',
      type = int,
      default = 0,
      choices = range(40, 256),
      help = 'limit line length to N characters (40 < N < 256)')
    args = parser.parse_args()

    if args.licensing in ['n', 'none']:
        licenselevel = 0
    elif args.licensing in ['r', 'referenced']:
        licenselevel = 1
    elif args.licensing in ['b', 'bsdtext']:
        licenselevel = 2
    elif args.licensing in ['h', 'hashedtext']:
        licenselevel = 3
    elif args.licensing in ['t', 'text']:
        licenselevel = 4
    else:
        print('Licensing "', args.licensing, '" unknown, ', errorhelp, sep = '')
        exit(1)

    SPDX2Disclosure(args.filename, licenselevel, args.checksums, args.numbered, args.preamble, args.verbose, args.width)

if __name__ == '__main__':
    main()
