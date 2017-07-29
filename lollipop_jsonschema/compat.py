import sys

PY2 = int(sys.version_info[0]) == 2

if PY2:
    iteritems = lambda d: d.iteritems()
    itervalues = lambda d: d.itervalues()
else:
    iteritems = lambda d: d.items()
    itervalues = lambda d: d.values()
