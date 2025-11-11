import json
import sys

def generate_md_report(input_path, output_path):
    with open(input_path, 'r') as f:
        data = json.load(f)

    project_name = data.get("project", "Unknown Project")

    with open(output_path, 'w') as out:
        out.write(f"# Project Report: {project_name}\n\n")
        out.write("## Tools Summary\n\n")

        for tool in data.get("tools", []):
            out.write(f"- **Workflow**: {tool.get('workflow','')} | **Run ID**: {tool.get('run_id','')} | **Domain**: {tool.get('domain','')}\n")

        if "classifications" in data:
            out.write("\n## Classifications\n")
            for cls in data["classifications"]:
                desc = cls.get("desc", "")
                ref = cls.get("ref", "")
                out.write(f"- {desc}\n  - [Reference Link]({ref})\n")

    print(f"✅ Markdown report generated at {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_md_report.py <input.json> <output.md>")
        sys.exit(1)
    generate_md_report(sys.argv[1], sys.argv[2])
