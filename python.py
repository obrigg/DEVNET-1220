import meraki

dashboard = meraki.DashboardAPI()
networks = dashboard.organizations.getOrganizationNetworks(organizationId=12345)

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