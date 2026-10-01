class ToolSelector:

    def __init__(self, tools):

        self.tools = tools

        self.capability_map = {
            "authentication_logs": "log_search",
            "user_information": "user_lookup",
            "network_reputation": "network_lookup",
            "file_analysis": "file_analysis"
        }

    def discover_tools(self):

        print("\n================================")
        print("ARGUS TOOL DISCOVERY")
        print("================================")

        if not self.tools:

            print("\nNo tools available.")

            return

        for tool in self.tools:

            print(f"\nTool: {tool.name}")
            print(f"Description: {tool.description}")

    def select_tool(self, objective):

        print("\n================================")
        print("ARGUS TOOL SELECTION")
        print("================================")

        print("\nInvestigation objective:")
        print(f"- {objective}")

        objective_lower = objective.lower()

        if (
            "login" in objective_lower
            or "authentication" in objective_lower
            or "failed login" in objective_lower
        ):

            capability = "authentication_logs"

        elif (
            "user" in objective_lower
            or "employee" in objective_lower
            or "account" in objective_lower
        ):

            capability = "user_information"

        elif (
            "ip" in objective_lower
            or "network" in objective_lower
            or "source address" in objective_lower
        ):

            capability = "network_reputation"

        elif (
            "file" in objective_lower
            or "malware" in objective_lower
            or "executable" in objective_lower
        ):

            capability = "file_analysis"

        else:

            print("\n[ARGUS]")
            print("Unable to determine the appropriate tool.")

            return None

        tool_name = self.capability_map.get(
            capability
        )

        print("\nRequired capability:")
        print(f"- {capability}")

        print("\nSelected tool:")
        print(f"- {tool_name}")

        return tool_name


if __name__ == "__main__":

    from tools.log_search import LogSearchTool
    from tools.user_lookup import UserLookupTool
    from tools.network_lookup import NetworkLookupTool
    from tools.file_analysis import FileAnalysisTool

    tools = [
        LogSearchTool(),
        UserLookupTool(),
        NetworkLookupTool(),
        FileAnalysisTool()
    ]

    selector = ToolSelector(tools)

    selector.discover_tools()

    objective = (
        "Investigate suspicious login activity involving Bob."
    )

    selected_tool = selector.select_tool(
        objective
    )

    print("\n================================")
    print("ARGUS RESULT")
    print("================================")

    if selected_tool:
        print(f"\nARGUS selected: {selected_tool}")
    else:
        print("\nARGUS could not select a tool.")