import os
import yaml

# Global Variable declaration block
masterValues = None
newValues = None
drift = None

def proc_owner():
    global newValues
    sd = {}
    owner = None
    svc = None

    stream = os.popen('ps aux')
    out = stream.read()
    lines = out.split('\n')
    lines = lines[1:]

    for line in lines:
        values = line.split()
        if len(values) > 10:
            if len(sd) == 0:
                owner = values[0]
                svc = values[10]
                sd[owner] = [svc]
            else:
                owner = values[0]
                svc = values[10]
                if owner in sd.keys():
                    k = sd[owner]
                    k.append(svc)
                else:
                    sd[owner] = [svc]
    newValues = sd
    with open('data.yml', 'w') as outfile:
        yaml.dump(newValues, outfile, default_flow_style=False)
    # return sd

if __name__ == '__main__':
    proc_owner()
