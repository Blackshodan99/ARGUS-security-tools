from tools.log_search import LogSearchTool
from tools.user_lookup import UserLookupTool
from tools.network_lookup import NetworkLookupTool
from tools.file_analysis import FileAnalysisTool

from tool_selector import ToolSelector
from evidence_store import EvidenceStore


def main():

    tools = [
        LogSearchTool(),
        UserLookupTool(),
        NetworkLookupTool(),
        FileAnalysisTool()
    ]

    selector = ToolSelector(tools)

    evidence_store = EvidenceStore()

    print("\n================================")
    print("ARGUS v0.3")
    print("MULTI-TOOL EVIDENCE COLLECTION")
    print("================================")

    selector.discover_tools()

    objective = (
        "Investigate suspicious login activity involving Bob."
    )

    selected_tool_name = selector.select_tool(
        objective
    )

    if not selected_tool_name:

        print("\n[ARGUS]")
        print("Investigation cannot continue.")

        return

    tool_map = {
        tool.name: tool
        for tool in tools
    }

    selected_tool = tool_map.get(
        selected_tool_name
    )

    if not selected_tool:

        print("\n[ARGUS]")
        print("Selected tool is not available.")

        return

    print("\n================================")
    print("ARGUS TOOL EXECUTION")
    print("================================")

    print(f"\nTool: {selected_tool.name}")
    print("Target: bob")

    log_results = selected_tool.run("bob")

    print("\nEvidence discovered:")

    for event in log_results:

        print(f"- {event}")

        evidence_store.add(
            "log_search",
            event
        )

    # =========================================================
    # EXTRACT SUSPICIOUS IP
    # =========================================================

    suspicious_ip = None

    for event in log_results:

        if "ip" in event:

            suspicious_ip = event["ip"]

            break

    if suspicious_ip:

        network_tool = tool_map.get(
            "network_lookup"
        )

        print("\n================================")
        print("ARGUS NETWORK INVESTIGATION")
        print("================================")

        print(
            f"\nInvestigating IP: {suspicious_ip}"
        )

        network_result = network_tool.run(
            suspicious_ip
        )

        print("\nNetwork evidence:")

        print(f"- {network_result}")

        evidence_store.add(
            "network_lookup",
            network_result
        )

    # =========================================================
    # DISPLAY COLLECTED EVIDENCE
    # =========================================================

    evidence_store.display()


if __name__ == "__main__":

    main()