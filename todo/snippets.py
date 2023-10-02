# SPDX-FileCopyrightText: 2023 Michael Weiblen http://mew.cx/
#
# SPDX-License-Identifier: MIT

# main.py


__version__ = "0.1.3.1"
__repo__ = "https://github.com/mew-cx/CircuitPython_dust_wx_station.git"

import busio
import time
import board
import sys
import wifi
import socketpool
from micropython import const

import adafruit_ds1307
import rtc
import adafruit_ntp

import rfc5424
from secrets import secrets

    def GetNtpTime(self):
        pool = socketpool.SocketPool(wifi.radio)
        ntp = adafruit_ntp.NTP(pool, tz_offset=0)
        print("ntp.datetime", ntp.datetime)
        rtc.RTC().datetime = ntp.datetime


# vim: set sw=4 ts=8 et ic ai:
