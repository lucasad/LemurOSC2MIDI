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

import liblo, rtmidi

class OSC2MIDI(liblo.ServerThread):
        def __init__(self,port):
            liblo.ServerThread.__init__(self, port)
            self.midiout = rtmidi.MidiOut()
            self.midiout.open_virtual_port('Lemur')
        def __enter__(self):
            return self

        def add(self, control):
            control.midiout = self.midiout
            control.register_methods(self)

        def __exit__(self, type, value, traceback):
            self.midiout.close_port()
            self.stop()
