import re
import os

def generate_mermaid():
    contract_path = 'XML_XSD_Contract_v2.3_Centralized 1.md'
    readme_path = 'README.md'
    
    if not os.path.exists(contract_path):
        print(f"Error: {contract_path} not found")
        return

    with open(contract_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    connections = []
    current_team = None
    in_table = False

    for line in lines:
        # Detect team section
        team_match = re.search(r'^###\s+\*\*Team\s+([^*]+)\*\*', line)
        if team_match:
            current_team = team_match.group(1).strip()
            in_table = False
            continue

        # Detect table start
        if '| Richting | Berichttype | Van/Naar |' in line:
            in_table = True
            continue

        if in_table and line.strip().startswith('|'):
            if '---' in line:
                continue
            
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 4:
                richting = parts[1].upper()
                berichttype = parts[2].replace('`', '').strip()
                van_naar = parts[3].strip()

                # Clean up van_naar (remove arrows and extra text)
                other_team = re.sub(r'[←→]', '', van_naar).strip()
                # Remove extra info like "(NIEUW - Option A)" or "← CRM"
                other_team = other_team.split('(')[0].strip()
                
                if current_team and other_team and berichttype:
                    # Clean team names
                    t1 = current_team.split('—')[0].strip()
                    t2 = other_team.split('—')[0].strip()

                    # Handle multiple message types
                    types = [t.strip() for t in berichttype.split(',')]
                    
                    for t in types:
                        if 'ONTVANGT' in richting:
                            connections.append((t2, t1, t))
                        elif 'VERZENDT' in richting or 'BROADCAST' in richting:
                            connections.append((t1, t2, t))

    # Deduplicate and group by sender/receiver
    grouped = {}
    teams = set()
    for sender, receiver, msg in connections:
        key = (sender, receiver)
        if key not in grouped:
            grouped[key] = set()
        grouped[key].add(msg)
        
        # Track all unique teams and their IDs
        s_id = re.sub(r'[^a-zA-Z0-9]', '_', sender)
        r_id = re.sub(r'[^a-zA-Z0-9]', '_', receiver)
        teams.add((s_id, sender))
        teams.add((r_id, receiver))

    # Generate Mermaid syntax
    mermaid = ["flowchart TB"]
    
    # Style definitions
    mermaid.append("    classDef core fill:#0b1f2a,color:#fff,stroke:#0a7ea4,stroke-width:4px;")
    mermaid.append("    classDef ops fill:#1e3a8a,color:#fff,stroke:#0a7ea4,stroke-width:2px;")
    mermaid.append("    classDef support fill:#2d3748,color:#fff,stroke:#718096,stroke-width:1px;")
    
    # Categorize teams
    core_teams = {"CRM", "Identity", "Requestor"}
    support_teams = {"Monitoring", "Mailing", "Heartbeat", "Alle teams", "Heartbeat team"}

    # Group connections to identify "Heartbeat-only" lines
    mermaid.append("\n    subgraph CORE [\"🔑 Core & Routing\"]")
    for t_id, t_name in sorted(list(teams)):
        if t_name in core_teams:
            mermaid.append(f"        {t_id}([\"{t_name}\"])")
    mermaid.append("    end")

    mermaid.append("\n    subgraph OPS [\"⚙️ Operational Teams\"]")
    for t_id, t_name in sorted(list(teams)):
        if t_name not in core_teams and t_name not in support_teams:
            mermaid.append(f"        {t_id}([\"{t_name}\"])")
    mermaid.append("    end")

    mermaid.append("\n    subgraph SUPPORT [\"📢 Support & Alerts\"]")
    for t_id, t_name in sorted(list(teams)):
        if t_name in support_teams:
            mermaid.append(f"        {t_id}([\"{t_name}\"])")
    mermaid.append("    end")

    mermaid.append("\n    %% Connections")
    for (s, r), msgs in sorted(grouped.items()):
        # Separate heartbeats from other messages
        heartbeats = {m for m in msgs if "heartbeat" in m.lower()}
        functional = msgs - heartbeats
        
        s_id = re.sub(r'[^a-zA-Z0-9]', '_', s)
        r_id = re.sub(r'[^a-zA-Z0-9]', '_', r)

        if functional:
            msg_label = "<br/>".join(sorted(list(functional)))
            mermaid.append(f"    {s_id} -- \"{msg_label}\" --> {r_id}")
        
        if heartbeats:
            # Use dotted lines for heartbeats to reduce noise
            mermaid.append(f"    {s_id} -. \"heartbeat\" .-> {r_id}")

    # Apply classes
    mermaid.append("\n    %% Styling classes")
    for t_id, t_name in sorted(list(teams)):
        if t_name in core_teams:
            mermaid.append(f"    class {t_id} core;")
        elif t_name in support_teams:
            mermaid.append(f"    class {t_id} support;")
        else:
            mermaid.append(f"    class {t_id} ops;")

    mermaid_str = "\n".join(mermaid)

    # Update README
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        start_marker = "<!-- NETWORK_MAP_START -->"
        end_marker = "<!-- NETWORK_MAP_END -->"
        
        if start_marker in content and end_marker in content:
            new_content = re.sub(
                f"{start_marker}.*?{end_marker}",
                f"{start_marker}\n\n```mermaid\n{mermaid_str}\n```\n\n{end_marker}",
                content,
                flags=re.DOTALL
            )
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("README.md updated with network map.")
        else:
            print("Markers not found in README.md. Please add <!-- NETWORK_MAP_START --> and <!-- NETWORK_MAP_END -->.")
    else:
        print("README.md not found.")

if __name__ == "__main__":
    generate_mermaid()
