# test_rpmupdatelist.py
#   Runs a test suite for rpmupdatelist.py
#
# This test suite is only effective within the leehuk/rpmtestrepo Docker
# images, as it expects rpmtestpackage-1.0 to be installed
#
# https://github.com/leehuk/rpmupdatelist

from rpmupdatelist import get_rpm_updates, print_rpm_updates
from types import *

class ArgparseObject(object):
    pass

def test_get_rpm_updates_retval():
    args = ArgparseObject()
    setattr(args, "disablerepo", "*")
    assert type(get_rpm_updates(args)) is ListType

def test_get_rpm_updates_norepos():
    args = ArgparseObject()
    setattr(args, "disablerepo", "*")
    assert len(get_rpm_updates(args)) == 0

def test_get_rpm_updates_rpmtestpackage_noupdate():
    args = ArgparseObject()
    setattr(args, "disablerepo", "*")
    setattr(args, "enablerepo", ["rpmtestrepo-1.0"])
    assert len(get_rpm_updates(args)) == 0

def test_get_rpm_updates_rpmtestpackage_update():
    args = ArgparseObject()
    setattr(args, "disablerepo", "*")
    setattr(args, "enablerepo", ["rpmtestrepo-1.1"])
    assert len(get_rpm_updates(args)) == 1

def test_get_rpm_updates_rpmtestpackage_update_type():
    args = ArgparseObject()
    setattr(args, "disablerepo", "*")
    setattr(args, "enablerepo", ["rpmtestrepo-1.1"])

    updates = get_rpm_updates(args)
    assert type(updates) is ListType
    update = updates[0]
    assert type(update) is DictType

def test_get_rpm_updates_rpmtestpackage_update_data():
    args = ArgparseObject()
    setattr(args, "disablerepo", "*")
    setattr(args, "enablerepo", ["rpmtestrepo-1.1"])

    updates = get_rpm_updates(args)
    update = updates[0]
    assert update["name"] == "rpmtestpackage"
    assert update["version"] == "1.1-1"
    assert update["repo"] == "rpmtestrepo-1.1"

def test_get_rpm_updates_rpmtestpackage_update_extradata():
    args = ArgparseObject()
    setattr(args, "disablerepo", "*")
    setattr(args, "enablerepo", ["rpmtestrepo-1.1"])

    updates = get_rpm_updates(args)
    update = updates[0]
    assert len(update.keys()) == 3
