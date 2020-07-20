import random
import time
lastoctet = random.randint(1,254)

def generate_ip():
    while True:
        vlan = input("Which VLAN would you like to create an IP address in?: ")
        try:
            int(vlan)
        except ValueError:
            print("VLAN must be a number")
            continue

        if 1 < int(vlan) < 255:
            print("Your VLAN " + str(vlan) + " IP address is 10.10." + str(vlan) + "." + str(lastoctet))
            break
        else:
            print("Number not a valid VLAN.")

print("Welcome to the IP address generator.")
print("For reference, each VLAN is split into /24 subnets, where the vlan number is the third octet.")

time.sleep(1)
generate_ip()