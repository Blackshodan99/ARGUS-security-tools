from tools.log_search import LogSearchTool
from tools.user_lookup import UserLookupTool
from tools.network_lookup import NetworkLookupTool
from tools.file_analysis import FileAnalysisTool

from tool_selector import ToolSelector


def main():

    tools = [
        LogSearchTool(),
        UserLookupTool(),
        NetworkLookupTool(),
        FileAnalysisTool()
    ]

    selector = ToolSelector(tools)

    print("\n================================")
    print("ARGUS v0.2")
    print("TOOL DISCOVERY AND SELECTION")
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

    result = selected_tool.run("bob")

    print("\nEvidence discovered:")

    if isinstance(result, list):

        for event in result:
            print(f"- {event}")

    else:

        print(f"- {result}")


if __name__ == "__main__":
    main()