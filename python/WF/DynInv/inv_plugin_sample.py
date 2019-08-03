# Copyright (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
    inventory: alan
    version_added: "2.5"
    short_description: Returns string "alan" for values of stuff
    description:
        - Ignores whatever you give it
        - Returns inventory containing "alan"
'''

EXAMPLES = r'''
    # ansible -i 'host1.example.com, host2' -m user -a 'name=me state=absent' all
'''

import os

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils._text import to_bytes, to_native
from ansible.parsing.utils.addresses import parse_address
from ansible.plugins.inventory import BaseInventoryPlugin


class InventoryModule(BaseInventoryPlugin):

    NAME = 'myplugin'

def parse(self, inventory, loader, path, cache=True):

     # call base method to ensure properties are available for use with other helper methods
     super(InventoryModule, self).parse(inventory, loader, path, cache)

     # this method will parse 'common format' inventory sources and
     # update any options declared in DOCUMENTATION as needed
     config = self._read_config_data(path)

     # if NOT using _read_config_data you should call set_options directly,
     # to process any defined configuration for this plugin,
     # if you don't define any options you can skip
     #self.set_options()

     # example consuming options from inventory source
     mysession = apilib.session(user=self.get_option('api_user'),
                                password=self.get_option('api_pass'),
                                server=self.get_option('api_server')
     )


     # make requests to get data to feed into inventory
     mydata = mysession.getitall()

     #parse data and create inventory objects:
     for colo in mydata:
         for server in mydata[colo]['servers']:
             self.inventory.add_host(server['name'])
             self.inventory.set_variable(server['name'], 'ansible_host', server['external_ip'])
