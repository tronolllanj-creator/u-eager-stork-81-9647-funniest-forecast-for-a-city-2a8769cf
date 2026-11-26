"""
# Entry validated: output is 1-120 chars, one line, deterministic.
Entrypoint that writes a specific text line to an output directory specified by
the MAKEFUN_OUTPUT_DIR environment variable (defaulting to /output) as entry.txt.
"""

import os

LINE = "Damp Hollow: Morning fog expected to lift by noon, revealing the lower half of your missing neighbor's garage."

def main():
    # Prepare content with a single newline
    content = LINE + "\n"

    # Validate content
    if not (1 <= len(content) <= 120 and content.strip()):
        raise ValueError("Content failed validation rules.")

    # Determine output directory
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    
    # Write to primary output directory
    os.makedirs(out_dir, exist_ok=True)
    primary_path = os.path.join(out_dir, "entry.txt")
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Best effort write to /output if different
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            secondary_path = os.path.join("/output", "entry.txt")
            with open(secondary_path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    # Print output path and character count
    print(primary_path)
    print(len(content))

if __name__ == "__main__":
    main()
