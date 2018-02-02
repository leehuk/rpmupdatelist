#!/usr/bin/env python
#
# rpmupdatelist.py
#	Lists available updates from enabled repos in JSON form
#
# https://github.com/leehuk/rpmupdatelist
# Copyright (C) 2017-2018 Lee H <lee@leeh.uk>

from __future__ import print_function

import argparse
import json
import os
import sys
import yum

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', dest='cache', help='Do not refresh metadata cache')
    parser.add_argument('--enablerepo', action='append', dest='enablerepo', help='Enable repositories (wildcards permitted)')
    parser.add_argument('--disablerepo', action='append', dest='disablerepo', help='Disable repositories (wildcards permitted)')
    args = parser.parse_args()
    return args

def get_rpm_updates(args):
    yb = yum.YumBase()
    yb.preconf.debuglevel=0
    yb.preconf.errorlevel=0

    yb.conf.cache = os.geteuid() != 0

    if hasattr(args, "disablerepo") and args.disablerepo != None:
        for name in args.disablerepo:
            yb.repos.disableRepo(name)

    if hasattr(args, "enablerepo") and args.enablerepo != None:
        for name in args.enablerepo:
            yb.repos.enableRepo(name)

    if hasattr(args, "cache") and args.cache != None:
        yb.cleanMetadata()
        yb.cleanSqlite()

    pkgupdates = []

    pkglist = yb.doPackageLists('updates')
    if pkglist.updates:
        for pkg in sorted(pkglist.updates):
            pkginfo = {}
            pkginfo['name'] = pkg.name
            pkginfo['version'] = pkg.printVer()
            pkginfo['repo'] = pkg.repoid
            pkgupdates.append(pkginfo)

    return pkgupdates

def print_rpm_updates(pkgupdates):
    print(json.dumps(pkgupdates))

if __name__ == '__main__':
    print_rpm_updates(get_rpm_updates(parse()))
