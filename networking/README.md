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
