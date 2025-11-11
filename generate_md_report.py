import json
import sys
from datetime import datetime

def generate_md_report(json_path, output_path):
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    project = data.get("project", "Unknown Project")

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(f"#  Project Report: {project}\n\n")
        out.write(f"**Generated on:** {datetime.utcnow().isoformat()} UTC\n\n")
        out.write("##  Tools Summary\n\n")

        tools_data = data.get("tools", [])

        # 🔹 Flatten nested lists if needed
        flattened = []
        for t in tools_data:
            if isinstance(t, list):
                flattened.extend(t)
            else:
                flattened.append(t)

        if not flattened:
            out.write("_No tools data found._\n")
            return

        for tool in flattened:
            if isinstance(tool, dict):
                out.write(f"- **Workflow**: {tool.get('workflow','')}  \n")
                out.write(f"  **Run ID**: {tool.get('run_id','')}  \n")
                out.write(f"  **Domain**: {tool.get('domain','')}  \n")
                out.write(f"  **Timestamp**: {tool.get('timestamp','')}  \n")
                out.write(f"  **Files Count**: {tool.get('file_count','')}  \n\n")

        out.write("---\n _Markdown report generated successfully._\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_md_report.py input.json output.md")
        sys.exit(1)

    generate_md_report(sys.argv[1], sys.argv[2])
