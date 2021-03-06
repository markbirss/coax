#!/usr/bin/env python

from common import create_serial, create_interface

with create_serial() as serial:
    interface = create_interface(serial, reset=False, poll_flush=False)

    print('Resetting interface...')

    version = interface.reset()

    print(f'Firmware version is {version}')
