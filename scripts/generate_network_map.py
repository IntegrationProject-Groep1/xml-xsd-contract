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
    for sender, receiver, msg in connections:
        key = (sender, receiver)
        if key not in grouped:
            grouped[key] = set()
        grouped[key].add(msg)

    # Generate Mermaid syntax
    mermaid = ["flowchart LR"]
    
    # Style definitions
    mermaid.append("    classDef team fill:#1e3a8a,color:#fff,stroke:#0a7ea4,stroke-width:2px;")
    mermaid.append("    classDef external fill:#0b1f2a,color:#fff,stroke:#2f855a,stroke-width:1px;")

    teams = set()
    for (s, r), msgs in grouped.items():
        msg_label = "<br/>".join(sorted(list(msgs)))
        # Replace problematic characters for Mermaid
        s_id = re.sub(r'[^a-zA-Z0-9]', '_', s)
        r_id = re.sub(r'[^a-zA-Z0-9]', '_', r)
        
        mermaid.append(f"    {s_id}([\"{s}\"]) -- \"{msg_label}\" --> {r_id}([\"{r}\"])")
        teams.add((s_id, s))
        teams.add((r_id, r))

    for t_id, t_name in teams:
        mermaid.append(f"    class {t_id} team;")

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
