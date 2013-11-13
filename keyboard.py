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

from control import *

class Keyboard(Control):
    NOTE_OFF  = 0x80
    NOTE_ON   = 0x90
    PITCH_BEND= 0xE0
    CTRL_CHNG = 0xB0
    MOD_WHEEL = 0x01

    def __init__(self, name, channel=0):
        Control.__init__(self, name)
        self.last = [0] * 72
        self.set_constants(channel)

    def set_constants(channel):
        self.NOTE_OFF  = NOTE_OFF   + channel
        self.NOTE_ON   = NOTE_ON    + channel
        self.PITCH_BEND= PITCH_BEND + channel
        self.CTRL_CHNG = CTRL_CHNG  + channel
        self.MOD_WHEEL = MOD_WHEEL

    @OSC_Method('/white/vel')
    def white_vel(self, path, args, types, src, data):
        for value,note in zip(args, range(0,73)):
            if args[note] != self.last[note]:
                midi_note = note+19
                midi_value = int(value*127)
                midi_message = [0, midi_note, midi_value]
                if value == 0.0:
                    midi_message[0] = self.NOTE_OFF
                else:
                    midi_message[0] = self.NOTE_ON
                self.midiout.send_message(midi_message)
        self.last = args

    @OSC_Method('/ModWheel/x', 'f')
    def ModWheel(path, args, types, src, data):
        mod = int(args[0]*0x3FFF)
        mod_lsb = mod_bend | 0x7F
        mod_msb = (mod_bend | 0x3f80) >> 7
        print 'ModWheel', int(args[0]*127)
        self.midiout.send_message([self.CTRL_CHNG, self.MOD_WHEEL, mod_lsb, mod_msb])

    @OSC_Method('/bend/x')
    def PitchBend(path, args, types, src, data):
        bend = int(args[0]*0x3FFF)
        bend_lsb = bend_bend | 0x7F
        bend_msb = (bend_bend | 0x3f80) >> 7
        print 'Pitch Bend', bend
        self.midiout.send_message([self.PITCH_BEND, bend_lsb, bend_msb])
