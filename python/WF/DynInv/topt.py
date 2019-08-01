import getopt
import sys

argz = sys.argv[1:]
# print(argz)

try:
      opts, args = getopt.getopt(argz,"h:d:")
except getopt.GetoptError:
    print 'usage: py.scrip -h <hostname> or -d <datacenter>'
    sys.exit(2)

print(argz)
print(args)
print(opts)