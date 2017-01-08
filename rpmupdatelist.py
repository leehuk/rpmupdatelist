#!/usr/bin/env python
#
# rpmupdatelist.py
#	Lists available updates from enabled repos
#
# https://github.com/leehuk/rpmupdatelist
#
# Copyright (C) 2017 Lee H <lee@leeh.uk>
# Released under the BSD 3-Clause License

from __future__ import print_function

import argparse
import json
import os
import sys
import yum

yb = yum.YumBase()
yb.preconf.debuglevel=0
yb.preconf.errorlevel=0

yb.conf.cache = os.geteuid() != 0

parser = argparse.ArgumentParser()
parser.add_argument('-c', action='store_true', dest='cache', help='Do not forcibly refresh metadata cache.')
args = parser.parse_args()

if not args.cache:
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

print(json.dumps(pkgupdates))
