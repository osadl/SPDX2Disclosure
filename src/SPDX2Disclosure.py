#!/usr/bin/env python

# This software is licensed under GPL-3.0
# Copyright (c) 2023 Open Source Automation Development Lab (OSADL) eG <info@osadl.org>
# Author Carsten Emde <C.Emde@osadl.org>

import argparse

def getlicenselist(filename):
    filename = filename.replace('-SPDX2TV.spdx', '-OSS-disclosure.txt')
    f = open(filename, 'r')
    licenselist = ''
    for line in f:
        licenselist += line
        if line.startswith('Copyright notices'):
            break;
    f.close()
    return licenselist

def collectlicenses(filename):
    licenses = {}
    f = open(filename, 'r')
    intext = False
    for line in f:
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
    return licenses

def SPDX2Disclosure(filename, licenselevel, verbose):
    if licenselevel == 0:
        print(getlicenselist(filename))
    else:
        licenses = collectlicenses(filename)

    f = open(filename, 'r')
    first = True
    infile = False
    incopyright = False
    for line in f:
        line = line.rstrip()
        if line.startswith('LicenseID: '):
            break
        if line.startswith('FileName: '):
            if verbose:
                print('Found entry of file ', line[10:].rstrip())
            copyrightnotice = ''
            licensenotice = []
            file = line[10:].rstrip()
            infile = True
            continue
        if infile:
            if line.startswith('LicenseInfoInFile: '):
                licensenotice.append(line[19:].strip())
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
                        for licensename in licensenotice:
                            if licensename != 'NOASSERTION':
                                haslicense = True
                                break
                    if copyrightnotice != 'NOASSERTION' or haslicense:
                        if first:
                            first = False
                        else:
                            print('-'*72)
                        print('FILE: ' + file + ':')
                        needsection = True
                    else:
                        if verbose:
                            print('Warning: Skipped file ' + file)
                            print()
                    if copyrightnotice != 'NOASSERTION':
                        if licenselevel > 0:
                            print('COPYRIGHT NOTICES:')
                        print(copyrightnotice)
                    if licenselevel > 0 and haslicense:
                        if len(copyrightnotice) > 0 and copyrightnotice != 'NOASSERTION':
                            print()
                        print('LICENSING:')
                        for licensename in licensenotice:
                            if licensename != 'NOASSERTION':
                                if licenselevel > 1:
                                    print(licensename + ':')
                                    print(licenses[licensename])
                                    print()
                                else:
                                    print(licensename)
                                needsection = True
                        licensenotice = []
                    copyrightnotice = ''
                    if needsection:
                        print()
    if licenselevel == 1:
        print()
        print('REFERENCED LICENSES:')
        for k in licenses:
            print(k + ':')
            print(licenses[k])
            print()
    f.close

def main():
    parser = argparse.ArgumentParser(prog = 'SPDX2Disclosure.py',
        epilog = 'Create several more verbose versions of the disclosure document from the SPDX tag:value file')

    parser.add_argument('filename',
      metavar = 'SPDX',
      help = 'file name of an SPDX tag:value input file to process')
    parser.add_argument('-l', '--licensing',
      metavar = 'VERBOSITY',
      default = 'none',
      help = 'add licensing information per file, may be "(n)one" (default), "(r)eferenced", or "(t)ext"')
    parser.add_argument('-v', '--verbose',
      action = 'store_true',
      default = False,
      help = 'show names and texts the program is using')
    args = parser.parse_args()

    if args.licensing not in ['n', 'none', 'r', 'referenced', 't', 'text']:
        print('Licensing "', args.licensing, '" unknown, must be either "(n)one", "(r)eferenced" or "(t)ext"', sep = '')
        exit(1)

    licenselevel = 0
    if args.licensing in ['r', 'referenced']:
        licenselevel = 1
    elif args.licensing in ['t', 'text']:
        licenselevel = 2

    SPDX2Disclosure(args.filename, licenselevel, args.verbose)

if __name__ == '__main__':
    main()
