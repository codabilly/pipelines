from WFServer import *
# from DynInv.WFServer import *
import csv
import yaml
import json
import time
import sys
import getopt

# Global Params

inventory = {'all': {}}
hosts = {'hosts': {}}
children = {'children': {}}

head = inventory.get('all')
head.update(hosts)
head.update(children)

# feed = open('feed.csv', mode='r', newline='')
feed = open('feed.csv', mode='r')

def buildNode(srv):
    node = {srv.fqn: {'ansible_host': srv.ip}}
    return node

def buildDataCenters(dtc, node, stub):
    entry = {dtc: node}
    keys = stub.keys()

    if dtc not in keys:
        stub.update({dtc: {'hosts': {}}})
        k = stub.get(dtc).get('hosts')
        k.update(node)
    else:
        k = stub.get(dtc).get('hosts')
        k.update(node)

try:
    opts, args = getopt.getopt(sys.argv[1:],"h:d:")
except getopt.GetoptError:
    print("We done screwed the pooch!")
    sys.exit(2)

time_stop_mills = 0
time_start_mills = int(round(time.time() * 1000))


# Parsing Strategy:
# Hostname:
#   As the reader will have to read all the rows and find the matching server's datacenter I believe the easiest way will be to parse the entire file and then just rebild the host portions from the datacenter level
#   should not be a huge as it in memory, maybe it can be improved who know, but for the time being this will be the way to do it.
# Datacenter:
#   This is the best approach! this can be accomplished in a singles pass and its the preferred way! Super easy!
rows = csv.reader(feed)
for row in rows:
    srv = WFServer(row[10], row[11], row[12], row[8], row[14], row[4], row[20])
    if srv.os != 'OS_SUPPORT':
        node = buildNode(srv)
        hosts.get('hosts').update(node)
        buildDataCenters(srv.dtc, node, children.get('children'))

# with open('endpoints.yml', 'w') as outfile:
#     # noalias_dumper = yaml.dumper.SafeDumper
#     # noalias_dumper.ignore_aliases = lambda self, data: True
#     # yaml.safe_dump(inventory, outfile, default_flow_style=False, Dumper=noalias_dumper)
#     # yaml.safe_dump(inventory, outfile, default_flow_style=False)
#     json.dump(inventory, outfile, indent=2)
#     time_stop_mills = int(round(time.time() * 1000))



# print(time_start_mills)
# print(time_stop_mills)
# print('Total execution time: ')
# print (time_stop_mills - time_start_mills)

# ---------------------SCRATCH------------------

# server = WFServer('blacky.els.com','blacky','192.168.1.21','Linux','Opensuse Leap 15','prod','Sendera - DTC')
# server.tostring()


# content = feed.readlines()
#
# for cnt in content:
#     print(cnt)
