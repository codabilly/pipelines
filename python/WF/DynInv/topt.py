# import getopt
# import sys

# argz = sys.argv[1:]
# # print(argz)

# try:
#       opts, args = getopt.getopt(argz,"h:d:")
# except getopt.GetoptError:
#     print 'usage: py.scrip -h <hostname> or -d <datacenter>'
#     sys.exit(2)

# print(argz)
# print(args)
# print(opts)

# inventory = {'all': {}}
# hosts = {'hosts': {}}
# hosts.get('hosts').update({ 'paradox':{} })
# print(hosts)
# children = {'children': {}}

# head = inventory.get('all')
# head.update(hosts)
# head.update(children)

# print(inventory)
# print(inventory.get('all').get('hosts'))

groups = []

groups.append('g1')
groups.append('b72')
groups.append('c3')

print(groups)