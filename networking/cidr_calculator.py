import ipaddress

cidr = input("Enter CIDR range: ")
network = ipaddress.ip_network(cidr)

print("Network:", network.network_address)
print("Subnet Mask:", network.netmask)
print("Prefix Length:", network.prefixlen)
print("Total IPs:", network.num_addresses)
print("Last Address:", network.broadcast_address)

if network.version == 4 and 4 <= network.prefixlen <= 29:
    print("GCP Usable Primary IPs:",
          network.num_addresses - 4)
else:
    print("Not a supported GCP primary IPv4 subnet size")
