import subprocess


def change_mac(interface, new_mac):
    # Bring the interface down
    subprocess.call(f"ifconfig {interface} down", shell=True)
    
    # Change the MAC address
    subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
    
    # Bring the interface up
    subprocess.call(f"ifconfig {interface} up", shell=True)

def main():
    interface = input("Enter the interface name: ")
    new_mac = input("Enter the new MAC address: ")

    # Display the current MAC address
    print("[*] Current MAC address:")
    subprocess.call("ifconfig", shell=True)

    # Change the MAC address
    change_mac(interface, new_mac)

    # Confirm the change
    print(f"[+] MAC address has been successfully changed to {new_mac}")
    subprocess.call("ifconfig", shell=True)


if __name__ == "__main__":
    main()
