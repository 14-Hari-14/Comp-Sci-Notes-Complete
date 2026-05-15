import os
import re

# Set this to the path of your notes folder
vault_path = "./2_Study_Notes/0_Core_Cs_Notes"

def migrate_to_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if YAML already exists
    if content.startswith("---"):
        return

    # Extract existing data using regex
    date_match = re.search(r'^Date:\s*(.*)', content, re.MULTILINE)
    topics_match = re.search(r'^Topics:\s*(.*)', content, re.MULTILINE)
    link_match = re.search(r'^Link:\s*(.*)', content, re.MULTILINE)
    class_match = re.search(r'^Class:\s*(.*)', content, re.MULTILINE)
    purpose_match = re.search(r'^Purpose:\s*(.*)', content, re.MULTILINE)

    # Clean up tags (convert "#ml #ai" to "ml, ai")
    tags = []
    if topics_match and topics_match.group(1).strip() != "#":
        raw_tags = topics_match.group(1).split()
        tags = [t.replace('#', '') for t in raw_tags]

    # Format into YAML
    yaml_lines = ["---"]
    if date_match and date_match.group(1): yaml_lines.append(f"date: {date_match.group(1).strip()}")
    if tags: yaml_lines.append(f"tags: [{', '.join(tags)}]")
    if link_match and link_match.group(1): yaml_lines.append(f"link: {link_match.group(1).strip()}")
    if class_match and class_match.group(1): yaml_lines.append(f"class: \"{class_match.group(1).strip()}\"")
    if purpose_match and purpose_match.group(1): yaml_lines.append(f"purpose: \"{purpose_match.group(1).strip()}\"")
    yaml_lines.append("---\n")

    yaml_block = "\n".join(yaml_lines)

    # Remove the old inline fields from the body
    content = re.sub(r'^(Date|Topics|Link|Class|Purpose):.*\n?', '', content, flags=re.MULTILINE)

    # Write the new structured file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(yaml_block + "\n" + content.lstrip())
    
    print(f"Migrated: {os.path.basename(filepath)}")

# Execute
for root, dirs, files in os.walk(vault_path):
    for file in files:
        if file.endswith(".md"):
            migrate_to_yaml(os.path.join(root, file))