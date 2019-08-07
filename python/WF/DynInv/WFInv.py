from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
    inventory: WFInv
    version_added: "2.8.1"
    short_description: Returns an inventory based on a PACK200 CSV feed
    description:
        This pluging parses a PACK2000 / Remedy CSV file and returns a 
        valid inventory object for consumption by Ansible.
'''

EXAMPLES = r'''
     ansible -i pack2000.csv -m ping all
'''

import os
import csv
import time

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils._text import to_bytes, to_native
from ansible.parsing.utils.addresses import parse_address
from ansible.plugins.inventory import BaseInventoryPlugin


feed = ''
groups = []

class WFServer:
    '''
    this is a utility class which handles the representation of a server once its parsed from the CSV file
    '''

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

class InventoryModule(BaseInventoryPlugin):

    NAME = 'WFInv'

    def verify_file(self, host_list):
        try:
            # read in the CSV file
            global feed
            feed = open(host_list, mode='r')
        except:
            print('Roh roh!')
            return True
        return True

    def parse(self, inventory, loader, host_list, cache=True):
        super(InventoryModule, self).parse(inventory, loader, host_list)

        # time_start_mills = int(round(time.time() * 1000))
        # time_stop_mills = 0

        rows = csv.reader(feed)
        for row in rows:
            srv = WFServer(row[10], row[11], row[12], row[8], row[14], row[4], row[20])

            if srv.dtc not in groups and srv.dtc != 'SA_FACILITY':
                groups.append(srv.dtc)
                inventory.add_group(srv.dtc)

            if srv.os != 'OS_SUPPORT':
                # print(str(srv.fqn) + ' ' + str(srv.dtc))
                self.inventory.add_host(srv.fqn, group=srv.dtc)
        
        # time_stop_mills = int(round(time.time() * 1000))
        # print('Total execution time: ' + str(time_stop_mills - time_start_mills))
