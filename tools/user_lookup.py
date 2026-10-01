class UserLookupTool:
    name = "user_lookup"

    description = (
        "Look up information about a user, including their department, "
        "normal device, and normal IP address."
    )

    def run(self, username):
        users = {
            "bob": {
                "username": "bob",
                "department": "Finance",
                "normal_device": "FIN-LAPTOP-07",
                "normal_ip": "10.20.15.42",
                "role": "Financial Analyst"
            },
            "alice": {
                "username": "alice",
                "department": "IT",
                "normal_device": "IT-LAPTOP-03",
                "normal_ip": "10.20.10.21",
                "role": "Systems Administrator"
            }
        }

        return users.get(
            username.lower(),
            {"error": "User not found"}
        )