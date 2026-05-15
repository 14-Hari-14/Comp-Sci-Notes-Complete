import os
import re

# Path to notes folder
vault_path = "./2_Study_Notes/0_Core_Cs_Notes"


def extract_field(content, field):
    """
    Extract first valid occurrence of a field.
    Ignores blank/template leftovers.
    """
    matches = re.findall(
        rf'^{field}:\s*(.*)$',
        content,
        re.MULTILINE
    )

    for match in matches:
        value = match.strip()

        # Ignore junk/template leftovers
        if value in ["", "#", "[[]]"]:
            continue

        # Ignore values that are just 'link' or start with 'link' (e.g. 'Link', 'Link:', 'Link:')
        low = value.lower()
        if low == "link" or low.startswith("link"):
            continue

        return value

    return ""


def migrate_to_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip files already migrated
    if content.startswith("---"):
        print(f"Skipped: {os.path.basename(filepath)}")
        return

    # Extract metadata
    date_value = extract_field(content, "Date")
    topics_raw = extract_field(content, "Topics")
    purpose_value = extract_field(content, "Purpose")

    # Parse topics into YAML list
    topics = []
    if topics_raw:
        parts = re.split(r'[,\s]+', topics_raw)
        topics = [
            p.lstrip('#').strip()
            for p in parts
            if p.strip()
        ]

    # Build YAML
    yaml_lines = [
        "---",
        f"created: {date_value}" if date_value else "created:",
    ]

    # Topics
    if topics:
        quoted_topics = ", ".join(f'"{t}"' for t in topics)
        yaml_lines.append(f"topics: [{quoted_topics}]")
    else:
        yaml_lines.append("topics: []")

    # Other fields
    yaml_lines.append("tags: []")
    yaml_lines.append("aliases: []")

    if purpose_value:
        yaml_lines.append(f'purpose: "{purpose_value}"')
    else:
        yaml_lines.append('purpose: ""')

    yaml_lines.append("---")

    yaml_block = "\n".join(yaml_lines)

    # Remove old metadata/template junk
    cleaned_content = re.sub(
        r'^(Date|Topics|Link|Class|Purpose):.*$\n?',
        '',
        content,
        flags=re.MULTILINE
    )

    # Clean extra whitespace at top
    cleaned_content = cleaned_content.lstrip()

    # Write updated file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(yaml_block + "\n\n" + cleaned_content)

    print(f"Migrated: {os.path.basename(filepath)}")


# Run migration
for root, dirs, files in os.walk(vault_path):
    for file in files:
        if file.endswith(".md"):
            migrate_to_yaml(os.path.join(root, file))


def sanitize_existing_purpose_links(vault_root):
    """
    Scan already-migrated files and clear `purpose` values that are just 'Link' or start with 'Link'.
    """
    for root, dirs, files in os.walk(vault_root):
        for file in files:
            if not file.endswith('.md'):
                continue
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Only operate on files with YAML frontmatter
            if not content.startswith('---'):
                continue

            # Find purpose line
            m = re.search(r'(?m)^purpose:\s*(?P<val>.*)$', content)
            if not m:
                continue
            val = m.group('val').strip().strip('"\'')
            if val == "":
                continue
            if val.lower().startswith('link'):
                # replace the whole purpose line with empty purpose
                new_content = re.sub(r'(?m)^purpose:\s*.*$', 'purpose: ""', content)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Sanitized purpose in: {os.path.basename(path)}")


# Run sanitize pass to fix previously migrated files
sanitize_existing_purpose_links(vault_path)