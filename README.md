# rpmupdatelist
Interrogates the system via the yum api to determine what updates
are available from the given repositories, returning data in JSON.

## Usage
```
usage: rpmupdatelist.py [-h] [-c] [--enablerepo ENABLEREPO]
                        [--disablerepo DISABLEREPO]

optional arguments:
  -h, --help            show this help message and exit
  -c                    Do not refresh metadata cache
  --enablerepo ENABLEREPO
                        Enable repositories (wildcards permitted)
  --disablerepo DISABLEREPO
                        Disable repositories (wildcards permitted)
```

## JSON Format
```
[
    {
        "repo":"reponame",
        "name":"packagename",
        "version":"packageversion"
    }

]
```

## Example
```
[root@26514eb7ad0c rpmupdatelist]# ./rpmupdatelist.py --disablerepo=* --enablerepo=rpmtestrepo-1.1
[{"repo": "rpmtestrepo-1.1", "version": "1.1-1", "name": "rpmtestpackage"}]
```
