class NetworkLookupTool:
    name = "network_lookup"

    description = (
        "Investigate an IP address and return information about "
        "its location, reputation, and whether it is known to the organization."
    )

    def run(self, ip_address):
        network_data = {
            "185.203.14.22": {
                "ip": "185.203.14.22",
                "country": "Unknown",
                "organization": "Unknown Hosting Provider",
                "reputation": "Suspicious",
                "known_to_organization": False
            },
            "10.20.15.42": {
                "ip": "10.20.15.42",
                "country": "Internal",
                "organization": "Company Network",
                "reputation": "Trusted",
                "known_to_organization": True
            }
        }

        return network_data.get(
            ip_address,
            {
                "ip": ip_address,
                "country": "Unknown",
                "organization": "Unknown",
                "reputation": "Unknown",
                "known_to_organization": False
            }
        )