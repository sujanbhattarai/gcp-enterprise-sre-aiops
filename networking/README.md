# Enterprise GCP Network Architecture

## VPC Configuration
- Name: enterprise-sre-vpc
- Mode: Custom
- Dynamic Routing: Regional
- Subnet Region: us-east4

## Primary Subnets
- Application: 10.10.1.0/24
- Management: 10.10.2.0/24
- Data: 10.10.3.0/24
- Monitoring: 10.10.4.0/24

## GKE Secondary Ranges
- Pods: 10.20.0.0/16
- Services: 10.30.0.0/20

## Security Design
- Private Google Access enabled
- Non-overlapping IP ranges
- Dedicated workload subnets
- Firewall rules planned for next phase

## Future Enhancements
- Cloud NAT
- Cloud Router
- Cloud DNS
- Private Service Connect
- Terraform automation

## VPC Routing
- System-generated subnet routes
- Default IPv4 internet route
- Regional dynamic routing mode
- Primary and secondary subnet routes
- No custom static routes required initially

## Routing Troubleshooting
- Validate destination IP and CIDR
- Review applicable routes and next hops
- Check firewall rules and priorities
- Validate DNS and application connectivity
- Review Cloud Router and BGP when applicable

## Cloud Router
- Name: enterprise-sre-router
- Network: enterprise-sre-vpc
- Region: us-east4
- Private ASN: 64514
- Dynamic Routing Mode: Regional
- Purpose: Dynamic routing and Cloud NAT configuration
- BGP Peers: Not configured

## Cloud Router Troubleshooting
- Validate router configuration
- Check BGP session status
- Review learned and advertised routes
- Validate VPN and Interconnect connectivity
- Investigate route withdrawals

## VPC Network Peering
- Primary VPC: enterprise-sre-vpc
- Partner VPC: partner-services-vpc
- Partner Subnet: 10.40.1.0/24
- Region: us-east4
- Peering: enterprise-to-partner
- Reverse Peering: partner-to-enterprise
- Purpose: Private cross-VPC communication

## VPC Peering Design Principles
- Non-overlapping subnet IP ranges
- Matching peering configurations
- Non-transitive connectivity
- Independent firewall management
- Private IP communication

## VPC Peering Troubleshooting
- Validate peering connection status
- Check subnet CIDR overlap
- Review exchanged routes
- Validate source and destination firewall rules
- Investigate DNS resolution
- Review application connectivity
