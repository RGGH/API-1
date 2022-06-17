
# Ask user how many interfaces to add
# Data Class type checks input data
# Payload will be sent via Python requests library

from dataclasses import dataclass
from typing import List


@dataclass
class InterfaceContext:

    interface_name: str
    interface_type: str
    profile_vector_name : str
    interface_id : str
    device_name : str
    lower_layer_interfaces : List
    bundle_name : str


def ask_user()->int:
    ''' Number of interfaces - for API payload'''
    qty_interfaces = (input("How Many Interfaces?\n"))
    if not qty_interfaces.isdigit():
        raise ValueError('Input is not number, cannot continue Execution')
    else:
        return int(qty_interfaces)


def generate_multiple_interfaces(qty_interfaces)->List:
    ''' Create interfaces 1 to 8 - and increment interface name (1 to 8)'''
    inst=[]
    for i in range(qty_interfaces+1):
        inst.append(InterfaceContext(f"SampleInterface-00{i}","generic","{{interfaces-pv-name}}",f"{i}","rooted-device",[
                    f"hundred-gigabit-ethernet 0/{i}"
                ],"{{interfaces-bundle-name}}"))

    return (inst)

def main():
    ''' Call functions to get the user input and generate payload for API '''
    try:
        qty_interfaces = ask_user()
    except ValueError as err:
        print (str(err))

    payload = generate_multiple_interfaces(qty_interfaces)
    print(payload) # comment out later
    return payload


# Main Driver
if __name__ == '__main__':

    main()
