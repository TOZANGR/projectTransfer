from scapy.all import ARP, Ether, srp
import socket

def find_devices_on_network(target_ip):
    # Create an ARP request to get the MAC address for each IP in the local network
    arp_request = ARP(pdst=target_ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine ARP and Ether packets
    packet = broadcast/arp_request
    # Send the packet and get a response
    result = srp(packet, timeout=3, verbose=False)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

def get_network_range():
    # Get your own IP address and determine network range
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    ip_parts = ip_address.split(".")
    # Typically, local networks use a 255.255.255.0 subnet
    network_range = f"10.179.67.1/24"  # Example: 192.168.1.1/24
    return network_range

network_range = get_network_range()
print(f"Scanning network: {network_range}")
def get_devices():
    devices = find_devices_on_network(network_range)
    return devices
