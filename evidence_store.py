class EvidenceStore:

    def __init__(self):

        self.evidence = []

    def add(self, source, data):

        evidence_item = {
            "source": source,
            "data": data
        }

        self.evidence.append(
            evidence_item
        )

    def get_all(self):

        return self.evidence

    def display(self):

        print("\n================================")
        print("ARGUS EVIDENCE STORE")
        print("================================")

        if not self.evidence:

            print("\nNo evidence collected.")

            return

        for item in self.evidence:

            print(f"\nSource: {item['source']}")
            print(f"Data: {item['data']}")


if __name__ == "__main__":

    store = EvidenceStore()

    store.add(
        "log_search",
        {
            "event": "Successful login",
            "user": "bob",
            "ip": "185.203.14.22"
        }
    )

    store.add(
        "network_lookup",
        {
            "ip": "185.203.14.22",
            "reputation": "Suspicious"
        }
    )

    store.display()