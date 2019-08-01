from WFServer import *
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

rows = ''
datacenter = ''
hostname = ''
time_stop_mills = 0
time_start_mills = 0

def buildNode(srv):
    node = {srv.fqn: {'ansible_host': srv.ip}}
    return node

def buildDataCenters(dtc, node, stub):
    keys = stub.keys()

    if dtc not in keys:
        stub.update({dtc: {'hosts': {}}})
        k = stub.get(dtc).get('hosts')
        k.update(node)
    else:
        k = stub.get(dtc).get('hosts')
        k.update(node)

def fullParse():
    rows = csv.reader(feed)
    for row in rows:
        srv = WFServer(row[10], row[11], row[12], row[8], row[14], row[4], row[20])
        if srv.os != 'OS_SUPPORT':
            node = buildNode(srv)
            hosts.get('hosts').update(node)
            buildDataCenters(srv.dtc, node, children.get('children'))

def parseForDataCenter():
    rows = csv.reader(feed)
    for row in rows:
        srv = WFServer(row[10], row[11], row[12], row[8], row[14], row[4], row[20])
        if srv.os != 'OS_SUPPORT':
            if srv.dtc == datacenter:
                node = buildNode(srv)
                hosts.get('hosts').update(node)
                buildDataCenters(srv.dtc, node, children.get('children'))

def parseForHost():
    hostsLists = [] # Stores WFServer Objects
    rows = csv.reader(feed)

    for row in rows:
        srv = WFServer(row[10], row[11], row[12], row[8], row[14], row[4], row[20])
        if srv.os != 'OS_SUPPORT':
            hostsLists.append(srv)
            if srv.name == hostname:
                datacenter = srv.dtc
            
    
    for h in hostsLists:
        if h.dtc == datacenter:
            node = buildNode(h)
            hosts.get('hosts').update(node)
            buildDataCenters(srv.dtc, node, children.get('children'))
    
    print(str(hostsLists[0]))
    print(datacenter)

def persisteData():
    with open('endpoints.yml', 'w') as outfile:
        # noalias_dumper = yaml.dumper.SafeDumper
        # noalias_dumper.ignore_aliases = lambda self, data: True
        # yaml.safe_dump(inventory, outfile, default_flow_style=False, Dumper=noalias_dumper)
        # yaml.safe_dump(inventory, outfile, default_flow_style=False)
        json.dump(inventory, outfile, indent=2)

if __name__ == "__main__":
    #read in the CSV file
    feed = open('feed.csv', mode='r')

    # Retrieve parameters passed in
    try:
        opts, args = getopt.getopt(sys.argv[1:],"h:d:")
    except getopt.GetoptError:
        print("We done screwed the pooch!")
        sys.exit(2)

    # Parse the switches passed to the script
    for s, v in opts:
        if s =='-d':
            datacenter = v
        elif s == '-h':
            hostname = v
    
    # Start the clock
    time_start_mills = int(round(time.time() * 1000))

    # Determine the strategy to follow
    if len(opts) == 0:
        fullParse()
    elif len(datacenter) > 0: #check for this are this has higher priority than hostname value
        print('Found data center option with a value of ' +str(args))
        parseForDataCenter()
    elif len(hostname) > 0:
        parseForHost()
    
    #Write the data out
    persisteData()
    print(datacenter)

    # Stop the clock
    time_stop_mills = int(round(time.time() * 1000))
    print('Total execution time: ' + str(time_stop_mills - time_start_mills))
