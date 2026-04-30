import re
import os

CANONICAL_TEAMS = [
    "CRM", "Kassa", "Frontend", "Planning", "Facturatie", 
    "Monitoring", "Mailing", "Identity"
]

def get_canonical_teams(text):
    found = []
    for team in CANONICAL_TEAMS:
        if re.search(rf'\b{team}\b', text, re.IGNORECASE):
            found.append(team)
    if not found:
        if "Alle teams" in text or "Alle-teams" in text:
            found.append("Alle teams")
        elif "Heartbeat" in text and "Monitoring" not in text:
            found.append("Heartbeat")
        elif "Requestor" in text:
            found.append("Requestor")
    return found

def clean_berichttype(text):
    parts = re.split(r'[,<>]', text)
    cleaned = []
    for p in parts:
        p = p.replace('`', '').strip()
        if re.match(r'^[a-z0-9_ ]+$', p, re.IGNORECASE) and len(p) < 40:
            cleaned.append(p)
    return cleaned

def generate_mermaid():
    contract_path = 'XML_XSD_Contract_v2.3_Centralized 1.md'
    readme_path = 'README.md'
    
    if not os.path.exists(contract_path):
        return

    with open(contract_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    connections = []
    current_teams = []
    in_quick_reference = False
    in_table = False

    for line in lines:
        if '##  QUICK REFERENCE' in line:
            in_quick_reference = True
            continue
        if in_quick_reference and (line.startswith('## Navigatie') or line.startswith('## 0.')):
            in_quick_reference = False
            break
        if not in_quick_reference:
            continue

        team_match = re.search(r'^###\s+\*\*Team\s+([^*]+)\*\*', line)
        if team_match:
            current_teams = get_canonical_teams(team_match.group(1))
            in_table = False
            continue

        if '| Richting | Berichttype | Van/Naar |' in line:
            in_table = True
            continue

        if in_table and line.strip().startswith('|'):
            if '---' in line:
                continue
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 4:
                richting = parts[1].upper()
                berichttype_raw = parts[2]
                van_naar = parts[3]
                other_teams = get_canonical_teams(van_naar)
                types = clean_berichttype(berichttype_raw)
                
                if current_teams and other_teams and types:
                    for ct in current_teams:
                        for ot in other_teams:
                            for t in types:
                                if 'ONTVANGT' in richting:
                                    connections.append((ot, ct, t))
                                else:
                                    connections.append((ct, ot, t))

    grouped = {}
    unique_teams = set()
    for sender, receiver, msg in connections:
        if sender == receiver and "heartbeat" in msg.lower():
            continue
        key = (sender, receiver)
        if key not in grouped:
            grouped[key] = set()
        grouped[key].add(msg)
        unique_teams.add(sender)
        unique_teams.add(receiver)

    mermaid = ["flowchart TB"]
    mermaid.append("    %% Style Definitions")
    mermaid.append("    classDef core fill:#0b1f2a,color:#fff,stroke:#0a7ea4,stroke-width:4px;")
    mermaid.append("    classDef ops fill:#1e3a8a,color:#fff,stroke:#0a7ea4,stroke-width:2px;")
    mermaid.append("    classDef support fill:#2d3748,color:#fff,stroke:#718096,stroke-width:1px;")
    
    core_names = {"CRM", "Identity", "Requestor"}
    support_names = {"Monitoring", "Mailing", "Heartbeat", "Alle teams"}

    def get_id(name):
        return re.sub(r'[^a-zA-Z0-9]', '_', name)

    mermaid.append("\n    subgraph CORE [\"🔑 Core & Routing\"]")
    for name in sorted(list(unique_teams)):
        if name in core_names:
            mermaid.append(f"        {get_id(name)}([\"{name}\"])")
    mermaid.append("    end")

    mermaid.append("\n    subgraph OPS [\"⚙️ Operational Teams\"]")
    for name in sorted(list(unique_teams)):
        if name not in core_names and name not in support_names:
            mermaid.append(f"        {get_id(name)}([\"{name}\"])")
    mermaid.append("    end")

    mermaid.append("\n    subgraph SUPPORT [\"📢 Support & Alerts\"]")
    for name in sorted(list(unique_teams)):
        if name in support_names:
            mermaid.append(f"        {get_id(name)}([\"{name}\"])")
    mermaid.append("    end")

    mermaid.append("\n    %% Functional Flows with Color Coding")
    link_styles = []
    link_count = 0

    for (s, r), msgs in sorted(grouped.items()):
        heartbeats = {m for m in msgs if "heartbeat" in m.lower()}
        functional = msgs - heartbeats
        s_id, r_id = get_id(s), get_id(r)

        if functional:
            msg_label = "<br/>".join(sorted(list(functional)))
            mermaid.append(f"    {s_id} -- \"{msg_label}\" --> {r_id}")
            
            # Color coding logic
            if s == "CRM":
                # Outgoing from CRM: Blue
                link_styles.append(f"    linkStyle {link_count} stroke:#3b82f6,stroke-width:2px,color:#3b82f6;")
            elif r == "CRM":
                # Incoming to CRM: Green
                link_styles.append(f"    linkStyle {link_count} stroke:#10b981,stroke-width:2px,color:#10b981;")
            else:
                # Other functional: Indigo
                link_styles.append(f"    linkStyle {link_count} stroke:#6366f1,stroke-width:2px,color:#6366f1;")
            link_count += 1
        
        if heartbeats:
            mermaid.append(f"    {s_id} -. \"heartbeat\" .-> {r_id}")
            # Heartbeats: Grey
            link_styles.append(f"    linkStyle {link_count} stroke:#94a3b8,stroke-width:1px,stroke-dasharray: 5 5,color:#94a3b8;")
            link_count += 1

    mermaid.append("\n    %% Styling Classes")
    for name in sorted(list(unique_teams)):
        t_id = get_id(name)
        if name in core_names:
            mermaid.append(f"    class {t_id} core;")
        elif name in support_names:
            mermaid.append(f"    class {t_id} support;")
        else:
            mermaid.append(f"    class {t_id} ops;")

    # Add the link styles at the end
    mermaid.append("\n    %% Edge Styles")
    mermaid.extend(link_styles)

    mermaid_str = "\n".join(mermaid)

    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        start, end = "<!-- NETWORK_MAP_START -->", "<!-- NETWORK_MAP_END -->"
        if start in content and end in content:
            new_content = re.sub(f"{start}.*?{end}", f"{start}\n\n```mermaid\n{mermaid_str}\n```\n\n{end}", content, flags=re.DOTALL)
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("README.md updated with COLOR CODED map.")

if __name__ == "__main__":
    generate_mermaid()
