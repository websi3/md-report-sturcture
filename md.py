import json

with open("summary/tools-summary.json") as f:
    data = json.load(f)

md = f"# Project Report: {data.get('project', 'unknown')}\n\n"
md += "## Tools Summary\n\n"

for t in data["tools"]:
    md += f"- **Tool:** {t.get('workflow','?')}\n"
    md += f"  - Run ID: `{t.get('run_id','?')}`\n"
    md += f"  - Domain/Target: `{t.get('domain', t.get('target','?'))}`\n"
    md += f"  - Timestamp: `{t.get('timestamp','?')}`\n"
    md += f"  - File Count: `{t.get('file_count','?')}`\n"
    md += "\n"

with open("project-reports/project-report.md", "w", encoding="utf-8") as f:
    f.write(md)
