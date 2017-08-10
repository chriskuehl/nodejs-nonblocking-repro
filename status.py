#!/usr/bin/env python2.7
"""Print the current stdout/stderr blocking mode."""
import fcntl, os, sys


def is_nonblocking(fileobj):
    flags = fcntl.fcntl(fileobj.fileno(), fcntl.F_GETFL)
    return bool(flags & os.O_NONBLOCK)


if __name__ == '__main__':
    status = {False: 'blocking', True: 'nonblocking'}
    print 'stdout is:', status[is_nonblocking(sys.stdout)]
    print 'stderr is:', status[is_nonblocking(sys.stderr)]
