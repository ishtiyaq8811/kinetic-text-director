#!/usr/bin/env python3
"""
Kinetic Typography Reel Director — Compiler & Injection Runner
Zero external pip dependencies. Injects JSON specs into template.html.
"""

import sys
import json
import os
import argparse
from pathlib import Path

def validate_spec(spec_data):
    """Simple robust schema validation without external dependencies."""
    required_keys = ["title", "phrases"]
    for key in required_keys:
        if key not in spec_data:
            raise ValueError(f"Missing required top-level key: '{key}'")
    
    if not isinstance(spec_data["phrases"], list) or len(spec_data["phrases"]) == 0:
        raise ValueError("'phrases' must be a non-empty array of phrase objects.")
    
    for idx, p in enumerate(spec_data["phrases"]):
        if "text" not in p or not isinstance(p["text"], str):
            raise ValueError(f"Phrase [{idx}] is missing valid 'text' string.")
        if "durationMs" not in p or not isinstance(p["durationMs"], (int, float)):
            raise ValueError(f"Phrase [{idx}] is missing valid 'durationMs' number.")
    
    return True

def compile_reel(spec_path, template_path=None, output_path=None):
    spec_path = Path(spec_path)
    if not spec_path.exists():
        print(f"Error: Spec file not found: {spec_path}", file=sys.stderr)
        return 1

    with open(spec_path, "r", encoding="utf-8") as f:
        spec_data = json.load(f)

    validate_spec(spec_data)
    print(f"✓ Validated spec: '{spec_data.get('title')}' ({len(spec_data['phrases'])} phrases)")

    if template_path is None:
        template_path = Path(__file__).parent / "template.html"
    else:
        template_path = Path(template_path)

    if not template_path.exists():
        print(f"Error: template.html not found at {template_path}", file=sys.stderr)
        return 1

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Inject spec payload
    injection = f"window.__KINETIC_SPEC__ = {json.dumps(spec_data, indent=2)};"
    compiled_html = template_content.replace(
        "const SPEC = window.__KINETIC_SPEC__ || {",
        f"{injection}\n    const SPEC = window.__KINETIC_SPEC__ || {{"
    )

    if output_path is None:
        stem = spec_path.stem
        output_path = spec_path.parent / f"{stem}.reel.html"
    else:
        output_path = Path(output_path)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(compiled_html)

    print(f"✓ Successfully compiled standalone reel: {output_path} ({len(compiled_html):,} bytes)")
    return 0

def main():
    parser = argparse.ArgumentParser(description="Kinetic Typography Reel Director Compiler")
    parser.add_argument("spec", help="Path to input JSON spec file")
    parser.add_argument("--template", "-t", help="Path to template.html", default=None)
    parser.add_argument("--output", "-o", help="Custom output HTML path", default=None)
    parser.add_argument("--validate", "-v", action="store_true", help="Validate spec only without building")

    args = parser.parse_args()

    if args.validate:
        with open(args.spec, "r", encoding="utf-8") as f:
            data = json.load(f)
        validate_spec(data)
        print(f"✓ Valid: {args.spec}")
        return 0

    return compile_reel(args.spec, args.template, args.output)

if __name__ == "__main__":
    sys.exit(main())