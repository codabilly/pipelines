from ansible.module_utils.basic import *
# from WF.DynInv.terter import *
from terter import *

def main():
	module = AnsibleModule(argument_spec={})
	response = terter.launch()
	module.exit_json(changed=False, meta=response)
	print(response)

if __name__ == '__main__':
    main()