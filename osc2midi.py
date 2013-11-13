#!/usr/bin/env python2
"""
© 2013 Lucas A. Dohring

This source code is licensed under the EUPL, Version 1.1 only (the “Licence”).
You may not use, modify or distribute this work except in compliance with the Licence.
You may obtain a copy of the Licence at:
<http://joinup.ec.europa.eu/software/page/eupl/licence-eupl>
A copy is also distributed with this source code.
Unless required by applicable law or agreed to in writing, software distributed under the
Licence is distributed on an “AS IS” basis, without warranties or conditions of any kind.
"""

from server import OSC2MIDI
from keyboard import Keyboard

server = OSC2MIDI(8000)
MasterKeyboard = Keyboard('/MasterKeyboard')
MasterKeyboard

server.add(MasterKeyboard)
server.start()

raw_input('Press any key to quit')
