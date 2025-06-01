import meraki

dashboard = meraki.DashboardAPI(suppress_logging=True)
networks = dashboard.organizations.getOrganizationNetworks(organizationId=3705899543372498445)
print (f"\n\nRetrieved {len(networks)} networks\n\n")

rules = [
    {
      "comment": "RDP to 1.2.3.0/24",
      "policy": "allow",
      "protocol": "tcp",
      "srcPort": "Any",
      "srcCidr": "Any",
      "destPort": "3389",
      "destCidr": "1.2.3.0/24",
      "syslogEnabled": False
    }
    ]

for network in networks:
    if "appliance" in network['productTypes']:
        dashboard.appliance.updateNetworkApplianceFirewallL3FirewallRules(networkId=network['id'], rules=rules)
        print (f"Applied rules on network {network['name']}")