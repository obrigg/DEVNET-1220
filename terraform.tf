terraform {
  required_providers {
    meraki = {
      version = "1.1.3-beta"
      source = "cisco-open/meraki"
    }
  }
}
provider "meraki" {
}

data "meraki_networks" "my_networks" {
  provider        = meraki
  organization_id = "12345"
}

resource "meraki_networks_appliance_firewall_l3_firewall_rules" "my_fw_rule" {
  for_each = {
    for idx, network in data.meraki_networks.my_networks.items : idx => network 
    if contains(network.product_types, "appliance")
  }

  provider                      = meraki
  network_id                    = each.value.id
  rules = [{
    comment        = "RDP to 1.2.3.0/24."
    dest_cidr      = "1.2.3.0/24"
    dest_port      = "3389"
    policy         = "allow"
    protocol       = "tcp"
    src_cidr       = "Any"
    src_port       = "Any"
    syslog_enabled = false
  }]
}
