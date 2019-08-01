#!/usr/bin/python
# A base representation of a server in the WF data centers


class WFServer:

    def __init__(self, fqn, name, ip, os, osv, env, dtc):
        self.fqn = fqn
        self.name = name
        self.ip = ip
        self.os = os
        self.osv = osv
        self.env = env
        self.dtc = dtc

    def __str__(self):
        return 'Server FQN: ' + self.fqn + ' Located in ' + self.dtc + ' running os: ' + self.os

    def tostring(self):
        print('Server FQN: ' + self.fqn + ' Located in ' + self.dtc + ' running os: ' + self.os)
