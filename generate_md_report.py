import json
import sys

def generate_md_report(json_path, output_path):
    with open(json_path) as f:
        data = json.load(f)

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(f"# Project Report: {data.get('project','')}\n\n")
        out.write("## Tools Summary\n\n")

        tools_data = data.get("tools", [])

        # Flatten if nested lists exist
        flattened = []
        for t in tools_data:
            if isinstance(t, list):
                flattened.extend(t)
            else:
                flattened.append(t)

        for tool in flattened:
            if isinstance(tool, dict):
                out.write(f"- **Workflow**: {tool.get('workflow','')} | **Run ID**: {tool.get('run_id','')} | **Domain**: {tool.get('domain','')}\n")

        out.write("\n Report generated successfully.\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_md_report.py input.json output.md")
        sys.exit(1)
    generate_md_report(sys.argv[1], sys.argv[2])
