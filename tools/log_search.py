class LogSearchTool:
    name = "log_search"

    description = (
        "Search authentication and security logs for users, "
        "IP addresses, and security events."
    )

    def run(self, query):
        logs = [
            {
                "time": "08:41",
                "event": "Failed login",
                "user": "bob",
                "ip": "185.203.14.22"
            },
            {
                "time": "08:42",
                "event": "Failed login",
                "user": "bob",
                "ip": "185.203.14.22"
            },
            {
                "time": "08:43",
                "event": "Failed login",
                "user": "bob",
                "ip": "185.203.14.22"
            },
            {
                "time": "08:44",
                "event": "Successful login",
                "user": "bob",
                "ip": "185.203.14.22"
            },
            {
                "time": "08:46",
                "event": "Command execution",
                "user": "bob",
                "ip": "185.203.14.22",
                "command": "powershell -ExecutionPolicy Bypass -File update.ps1"
            },
            {
                "time": "08:47",
                "event": "File download",
                "user": "bob",
                "ip": "185.203.14.22",
                "filename": "invoice_update.exe"
            }
        ]

        query = query.lower()

        return [
            event
            for event in logs
            if (
                event.get("user", "").lower() == query
                or event.get("ip", "").lower() == query
                or event.get("event", "").lower() == query
            )
        ]